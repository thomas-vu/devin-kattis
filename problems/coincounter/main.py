import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to get binary coins
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours of the coins
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize the sum of the coins
total_sum = 0

# Iterate through each contour and determine the coin value
for contour in contours:
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Check the size of the bounding rectangle to determine the coin value
    if w * h >= 100 and w * h <= 200:
        total_sum += 1
    elif w * h >= 350 and w * h <= 450:
        total_sum += 5
    elif w * h >= 800 and w * h <= 1000:
        total_sum += 10

# Output the sum of the coins
print(total_sum)