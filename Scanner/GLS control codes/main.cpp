//#include "stdafx.h"
#include <stdio.h>
#include "../raylase_includes/include/ClientAPI.h"

#define CARD_IP "192.168.1.141"

static rlResult markSquare( rlHandle handle );
static int printLastError( void );


int main()
{
	// establish a connection with the card
	rlHandle handle = rlConnect( CARD_IP, 49374 );
	if ( handle < 0 )
		return printLastError();

	rlResult status;

	// Reset the card to its default settings:
	// This restores the following settings to the values that were last saved on the card:
	// - scanner configuration (such as field size, field correction, etc.)
	// - laser configuration (such as gate/LM timing parameters, power target, etc.)
	// - process variables (such as jump speed, settling times, mark speed, etc.)
	if ( ( status = rlSystemResetToDefaults( handle ) ) != rlSUCCESS )
		goto Cleanup;

	// Set the laser power to 25%
	rlLaserConfig lc;
	if ( ( status = rlLaserGetConfig( handle, &lc ) ) != rlSUCCESS ) goto Cleanup;
	lc.PowerScale = 0.25;
	if ( ( status = rlLaserSetConfig( handle, &lc ) ) != rlSUCCESS ) goto Cleanup;

	// Enable the laser so it responds to commands that turn on the laser.
	// Note that this does not fire the laser until e.g. LaserOn or Mark command is executed.
	if ( ( status = rlLaserArmLaser( handle, true ) ) != rlSUCCESS ) goto Cleanup;

	// do the real work here
	while(1){
        status = markSquare( handle );
	}


Cleanup:
	// print any errors
	if ( status != rlSUCCESS )
		printLastError();

	// disconnect from the card
	printf( "Disconnecting from card...\n" );
	if ( rlDisconnect( handle ) != rlSUCCESS )
		return printLastError();

	printf( "Exiting with status = %d\n", status );
	return status;
}

static rlResult markSquare( rlHandle handle )
{
	rlResult result;

	// get the scanner's current field size
	rlScannerConfig sc;
	if ( ( result = rlScannerGetConfig( handle, &sc ) ) != rlSUCCESS )
		return result;
    printf("%f", sc.FieldSize.X);
	double squareSize = 750000;//32760 / 32768.0 * sc.FieldSize.X;

	double jumpSpeed = 30.0;
	double markSpeed = 1.0;

	// Create a list locally on the host computer,
	// and fill it with macro-vectors defining a square.
	int listIndex = 0;
	printf( "Preparing list: index=%d...\n", listIndex );
	rlCommandListHandle list = rlListAllocate( handle );

	if ( ( result = rlListAppendPower( list, 65535 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpSpeed( list, jumpSpeed ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendMarkSpeed( list, markSpeed ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, 0, 0 ) ) != rlSUCCESS )
//		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize / 2, -squareSize / 2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, -squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, squareSize/2 ) ) != rlSUCCESS )
		return result;
	if ( ( result = rlListAppendJumpAbs2D( list, squareSize/2, -squareSize/2 ) ) != rlSUCCESS )
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

// helper function which displays the description of the last error
static int printLastError( void )
{
	char errBuffer[1024] = { 0 };
	rlGetLastError( errBuffer, sizeof( errBuffer ) - 1 );
	printf( "%s", errBuffer );
	return rlERROR;
}
