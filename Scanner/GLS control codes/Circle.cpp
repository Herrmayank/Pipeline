#include <stdio.h>
#include "../raylase_includes/include/ClientAPI.h"

#define CARD_IP "192.168.1.141"//169.254.181.224

static rlResult markSquare( rlHandle handle );
static int printLastError( void );


#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <thread>
#include <queue>
#include <cmath>
#include <csignal>

using namespace std;

const string FILE_PATH = "E:/Masterarbeit/scannercoords.txt";
const int BUFFER_SIZE = 2;

bool terminatePrinting = false;

/*struct Job {
    unsigned long trackingID = 0;
    double startX = 0.0;
    double startY = 0.0;
    double duration = 0.0;
    double velocityX = 0.0;
    double velocityY = 0.0;
    int power = 0;

    Job() {}
    Job(unsigned long id, double x, double y, double t, double velX, double velY, int pow) :
        trackingID(id), startX(x), startY(y), duration(t), velocityX(velX), velocityY(velY), power(pow) {}
};*/ //Actual part of the code
Job quadJob;
quadJob.startX = 365000.0;  // Right boundary of the quadrilateral
quadJob.startY = 365000.0;  // Upper boundary of the quadrilateral
quadJob.duration = 1.0;     // Duration of the marking job (in seconds)
quadJob.velocityX = 0.0;    // No x-direction velocity (stationary)
quadJob.velocityY = 0.0;    // No y-direction velocity (stationary)
quadJob.power = 100;        // Laser power (adjust as needed)

Job buffer[BUFFER_SIZE];
int bufferIndex = 0;
unsigned long lastTrackingID = 0;
bool quit_requested = false;

void signal_handler(int signal)
{
    switch (signal) {
        case SIGINT:
            std::cout << "Received SIGINT signal (Ctrl+C)" << std::endl;
            break;
        case SIGTERM:
            std::cout << "Received SIGTERM signal" << std::endl;
            break;
        default:
            std::cout << "Received unknown signal" << std::endl;
            break;
    }

    // Set the quit flag to true to exit the while loop
    quit_requested = true;
}

static rlResult processJob(rlHandle handle, Job job, int& numJobsProcessed) {
    // simulate processing time
    //this_thread::sleep_for(chrono::milliseconds(100));

    //cout << "Processing job with Tracking ID: " << job.trackingID << endl;

    // increment the job counter
    numJobsProcessed++;
    rlResult result;

	// get the scanner's current field size
	rlScannerConfig sc;
	if ( ( result = rlScannerGetConfig( handle, &sc ) ) != rlSUCCESS )
		return result;

	double jumpSpeed = 7.5;//constant
	double markSpeed = 1.0;//variable

	// Create a list locally on the host computer,
	// and fill it with macro-vectors defining a square.
	int listIndex = 0;
	printf( "Preparing list: index=%d...\n", listIndex );
	rlCommandListHandle list = rlListAllocate( handle );

	double StartX = job.startX;
    double StartY = job.startY;
	double velX = job.velocityX;
    double velY = job.velocityY;
    double time = job.duration; // Sekunden

    double vel_mps = sqrt(pow(job.velocityX, 2) + pow(job.velocityY, 2));
    double endX = job.startX + velX * 1000000 * time;
    double endY = job.startY + velY * 1000000 * time;

    printf("StartX_Scanner in µm: %f\n", job.startX);
    printf("StartY_Scanner in µm: %f\n", job.startY);
    printf("EndX in µm: %f\n", endX);
    printf("EndY in µm: %f\n", endY);

    markSpeed = vel_mps;

    if(endX < -sc.FieldSize.X/2){
    	endX = -sc.FieldSize.X/2;
    }
    if(endX > sc.FieldSize.X/2){
    	endX = sc.FieldSize.X/2;
    }
    if(endY < -sc.FieldSize.Y/2){
    	endY = -sc.FieldSize.Y/2;
    }
    if(endY > sc.FieldSize.Y/2){
    	endY = sc.FieldSize.Y/2;
    }
    if(job.startX < -sc.FieldSize.X/2){
    	job.startX = -sc.FieldSize.X/2;
    }
    if(job.startX > sc.FieldSize.X/2){
    	job.startX = sc.FieldSize.X/2;
    }
    if(job.startY < -sc.FieldSize.Y/2){
    	job.startY = -sc.FieldSize.Y/2;
    }
    if(job.startY > sc.FieldSize.Y/2){
    	job.startY = sc.FieldSize.Y/2;
    }

	printf("markSpeed in m/s: %f\n", markSpeed);


	if ( ( result = rlListAppendPower( list, 0 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpSpeed( list, jumpSpeed ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, job.startX, job.startY ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendMarkSpeed( list, markSpeed ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendPower( list, job.power ) ) != rlSUCCESS )//65535
		return result;
	if(vel_mps!=0){
		if ( ( result = rlListAppendMarkAbs2D( list, endY, endX ) ) != rlSUCCESS )
			return result;
	}
	else{
		printf("TEST\n");
		if ( ( result = rlListAppendSleep( list, time * 1000000 ) ) != rlSUCCESS )
			return result;
	}
	if ( ( result = rlListAppendPower( list, 0 ) ) != rlSUCCESS )
		return result;


	// close the list causing its contents to be transferred to the card
	printf( "Closing list: index=%d...\n", listIndex );
	if ( ( result = rlListSet( handle, listIndex, list, false, -1 ) ) != rlSUCCESS )
		return result;

	// run the list, and wait until its execution has completed
	printf( "Executing list: index=%d...\n", listIndex );
	if ( ( result = rlListExecute( handle, listIndex ) ) != rlSUCCESS )
		return result;

	int timeoutMs = 30000;
	bool done = false;
	int32_t listID;
	printf( "Waiting until list execution is done: index=%d...\n", listIndex );
	if ( ( result = rlListWaitForListDone( handle, timeoutMs, &done, &listID ) ) != rlSUCCESS )
		return result;
	if ( !done )
	{
		printf( "Timeout: execution has not completed after %d ms!", timeoutMs );
		return rlERROR;
	}
	printf( "Execution done: index=%d...\n", listIndex );

	// delete list on the card: this frees the card's memory occupied by the list
	printf( "Deleting list: index=%d...\n", listIndex );
	if ( ( result = rlListDelete( handle, listIndex, true ) ) != rlSUCCESS )
		return result;

	// release the local list: this frees the PC's memory occupied by the card
	if ( ( result = rlListReleaseHandle( list ) ) != rlSUCCESS )
		return result;

	return result;
}

void checkForChanges(std::queue<Job>& job_buffer, std::string file_path) {
    std::ifstream file(file_path);
    if (file.is_open()) {
        std::string line;
        getline(file, line);
        file.close();

        // parse the line and create a job
        unsigned long tracking_id;
        double start_x, start_y, duration, velocity_x, velocity_y;
        int power_pow;
        sscanf(line.c_str(), "%lu %lf %lf %lf %lf %lf %d", &tracking_id, &start_x, &start_y, &duration, &velocity_x, &velocity_y, &power_pow);

        // check if the job is different than the last job
        if (tracking_id != lastTrackingID) {
            // put the new job in the buffer
            if (job_buffer.size() < 2) {
                Job new_job(tracking_id, start_x, start_y, duration, velocity_x, velocity_y, power_pow);
                job_buffer.push(new_job);
                std::cout << "New job added to buffer with Tracking ID: " << tracking_id << std::endl;
            }
            else {
                std::cout << "Buffer is full, new job with Tracking ID: " << tracking_id << " could not be added" << std::endl;
            }

            // update the last tracking ID
            lastTrackingID = tracking_id;
        }
    }
}

void printNumJobsProcessed(const int& numJobsProcessed, const bool& terminatePrinting) {
    while (!terminatePrinting) {
        cout << "Number of processed jobs: " << numJobsProcessed << endl;
        this_thread::sleep_for(chrono::seconds(5));
    }
}

int cleanup(rlResult status, rlHandle handle){

	if ( status != rlSUCCESS )
		printLastError();


	if ( rlLaserLaserOff( handle ) != rlSUCCESS )
		return printLastError();
	if ( rlLaserArmLaser( handle, false ) != rlSUCCESS )
		return printLastError();

	printf( "Disconnecting from card...\n" );
	if ( rlDisconnect( handle ) != rlSUCCESS )
		return printLastError();

	return status;
}

int main() {
    std::queue<Job> jobQueue;
    int numJobsProcessed = 0; // initialize the counter
    bool terminatePrinting = false; // initialize the printing termination flag

    // Register the signal handler for SIGINT and SIGTERM signals
    std::signal(SIGINT, signal_handler);
    std::signal(SIGTERM, signal_handler);

    // start the printing thread
    std::thread printingThread(printNumJobsProcessed, std::ref(numJobsProcessed), std::ref(terminatePrinting));

	rlHandle handle = rlConnect( CARD_IP, 49374 );
	if ( handle < 0 )
		return printLastError();

	rlResult status;

	if ( ( status = rlSystemResetToDefaults( handle ) ) != rlSUCCESS )
		cleanup(status, handle);

	rlLaserConfig lc;
	if ( ( status = rlLaserGetConfig( handle, &lc ) ) != rlSUCCESS ) cleanup(status, handle);
	lc.PowerScale = 1.00;
	if ( ( status = rlLaserSetConfig( handle, &lc ) ) != rlSUCCESS ) cleanup(status, handle);

	if ( ( status = rlLaserArmLaser( handle, true ) ) != rlSUCCESS ) cleanup(status, handle);

	char input;

    while (!quit_requested) {

    	checkForChanges(jobQueue, FILE_PATH);

        // process the first job in the buffer
        if (!jobQueue.empty()) {
            status = processJob(status, jobQueue.front(), numJobsProcessed);
            jobQueue.pop();
        }

        /*std::cin >> input;
        if (input == 'q') {
            quit_requested = true;
        }*/

        // wait for a short time before checking again
        //this_thread::sleep_for(chrono::milliseconds(10));
    }

    // set the printing thread termination flag and wait for it to finish
    terminatePrinting = true;
    printingThread.join();

    std::cout << "Exiting..." << std::endl;
    cleanup(status, handle);

    return status;

/*Cleanup:
	if ( status != rlSUCCESS )
		printLastError();

	printf( "Disconnecting from card...\n" );
	if ( rlDisconnect( handle ) != rlSUCCESS )
		return printLastError();

	printf( "Exiting with status = %d\n", status );
	return status;*/
}

// helper function which displays the description of the last error
static int printLastError( void )
{
	char errBuffer[1024] = { 0 };
	rlGetLastError( errBuffer, sizeof( errBuffer ) - 1 );
	printf( "%s", errBuffer );
	return rlERROR;
}
