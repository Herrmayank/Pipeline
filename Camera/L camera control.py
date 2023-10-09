import pyzed.sl as sl
import cv2


def main():
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.camera_fps = 30

    # Open the left camera
    zed_left = sl.Camera()
    if not zed_left.is_opened():
        print("Opening Left Camera...")
    status = zed_left.open(init_params)
    if status != sl.ERROR_CODE.SUCCESS:
        print(repr(status))
        exit()

    runtime_parameters = sl.RuntimeParameters()
    while True:
        # Grab frames from the left camera
        if zed_left.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            left_image = sl.Mat()
            zed_left.retrieve_image(left_image, sl.VIEW.LEFT)

            # Convert the image to a format suitable for OpenCV
            left_image_opencv = left_image.get_data()

            # Display the left camera frame using OpenCV
            cv2.imshow("Left Camera", left_image_opencv)

            # Wait for a key press and exit the loop if 'q' is pressed
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    zed_left.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()