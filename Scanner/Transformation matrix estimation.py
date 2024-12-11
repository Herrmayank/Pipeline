import numpy as np


def estimate_transformation_matrix(kp1, kp2, matches):
    # Extract location of good matches
    points1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    points2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Estimate transformation matrix (Affine or Homography)
    matrix, mask = cv2.findHomography(points1, points2, cv2.RANSAC, 5.0)

    return matrix


# Example usage
transformation_matrix = estimate_transformation_matrix(kp1, kp2, matches)
print("Transformation Matrix:")
print(transformation_matrix)
