import pyzed.sl as sl
import cv2


def main():
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.camera_fps = 30

    # Open the right camera
    zed_right = sl.Camera()
    if not zed_right.is_opened():
        print("Opening Right Camera...")
    status = zed_right.open(init_params)
    if status != sl.ERROR_CODE.SUCCESS:
        print(repr(status))
        exit()

    runtime_parameters = sl.RuntimeParameters()
    while True:
        # Grab frames from the right camera
        if zed_right.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            right_image = sl.Mat()
            zed_right.retrieve_image(right_image, sl.VIEW.RIGHT)

            # Convert the right image to a format suitable for OpenCV
            right_image_opencv = right_image.get_data()

            # Display the right camera frame using OpenCV
            cv2.imshow("Right Camera", right_image_opencv)

        # Wait for a key press and exit the loop if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    zed_right.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
