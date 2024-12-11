import cv2

def match_features_sift(image1_path, image2_path):
    # Read images
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect SIFT features in both images
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

    # Create feature matcher
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors
    matches = bf.match(descriptors_1, descriptors_2)

    # Sort them in the order of their distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 10 matches
    result = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:10], None)

    # Save the result
    cv2.imwrite("sift_result.png", result)

    return keypoints_1, keypoints_2, matches

# Example usage
kp1, kp2, matches = match_features_sift("path_to_image1.png", "path_to_image2.png")
