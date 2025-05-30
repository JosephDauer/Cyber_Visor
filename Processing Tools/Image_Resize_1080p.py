# simple image resize
import cv2

image = cv2.imread('image.jpg')
image = cv2.resize(image, (1920, 1080))  # Resize to 1080p
#normalized_image = resized_image / 255.0  # Normalize to [0, 1]
cv2.imwrite('resized_image.jpg', normalized_image * 255)  # Save the image
