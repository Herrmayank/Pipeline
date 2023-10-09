import pyzed.sl as sl
import cv2
import cv2.aruco as aruco
import numpy as np
import yaml

# Function to detect and draw the Charuco board
def detect_charuco(image, board):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    parameters = cv2.aruco.DetectorParameters_create()
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if len(corners) > 0:
        retval, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(
            corners, ids, gray, board)
        if retval > 0:
            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.aruco.drawDetectedCornersCharuco(image, charuco_corners, charuco_ids)

    return image

# Calibration parameters
squaresX = 6
squaresY = 8
squareLength = 0.04
markerLength = 0.02
output_file = "right_camera_calibration_values.yml"

# ZED camera initialization (right camera)
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720
init_params.camera_fps = 30

zed = sl.Camera()
if not zed.is_opened():
    print("Opening Right Camera...")
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS:
    print(repr(status))
    exit()


aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250)
board = cv2.aruco.CharucoBoard_create(
    squaresX=squaresX,
    squaresY=squaresY,
    squareLength=squareLength,
    markerLength=markerLength,
    dictionary=aruco_dict
)

obj_points = []  # Initialize as empty lists
img_points = []

cv2.namedWindow("Live Camera View", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Camera View", 800, 600)

while True:
    # Grab frames from the ZED camera
    runtime_parameters = sl.RuntimeParameters()
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        right_image = sl.Mat()
        zed.retrieve_image(right_image, sl.VIEW.RIGHT)
        right_image_opencv = right_image.get_data()

        # Ensure the image is in grayscale format
        if len(right_image_opencv.shape) == 3:
            gray = cv2.cvtColor(right_image_opencv, cv2.COLOR_BGR2GRAY)
        else:
            gray = right_image_opencv

        # Detect and draw the Charuco board
        detected_image = detect_charuco(gray, board)

        cv2.imshow("Live Camera View", detected_image)

        key = cv2.waitKey(1)
        if key == ord('c'):
            if len(obj_points) < 10:
                continue

            # Convert lists of points to NumPy arrays
            obj_points = [np.array(points).reshape(-1, 3) for points in obj_points]
            img_points = [np.array(points).reshape(-1, 2) for points in img_points]

            ret, mtx, dist, _, _ = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

            # Save calibration values to a YAML file
            with open(output_file, 'w') as yaml_file:
                data = {
                    'camera_matrix': mtx.tolist(),
                    'distortion_coefficients': dist.tolist()
                }
                yaml.dump(data, yaml_file)

            print("Calibration matrix:")
            print(mtx)

            print("Distortion coefficients:")
            print(dist)
            break

        # Append detected Charuco corners for calibration
        corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
        if len(corners) > 0:
            retval, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(
                corners, ids, gray, board)
            if retval > 0:
                obj_points.append(board.chessboardCorners)
                img_points.append(charuco_corners)

zed.close()
cv2.destroyAllWindows()
