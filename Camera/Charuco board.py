import cv2
import cv2.aruco as aruco

def create_charuco_board(squaresX, squaresY, squareLength, markerLength, image_size, output_file):
    # Create the Aruco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

    # Create the Charuco board
    gridboard = aruco.CharucoBoard_create(
        squaresX=squaresX,
        squaresY=squaresY,
        squareLength=squareLength,
        markerLength=markerLength,
        dictionary=aruco_dict
    )

    # Create an image from the gridboard
    board_image = gridboard.draw(image_size)

    # Save the Charuco board image
    cv2.imwrite(output_file, board_image)

    # Display the image
    cv2.imshow('Gridboard', board_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Define the board parameters
squaresX = 6
squaresY = 8
squareLength = 0.04
markerLength = 0.02
image_size = (988, 1400)
output_file = "test_charuco.jpg"

# Call the function to create the Charuco board
create_charuco_board(squaresX, squaresY, squareLength, markerLength, image_size, output_file)
