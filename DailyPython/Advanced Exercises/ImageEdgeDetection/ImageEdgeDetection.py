# The program loads an image file, image1.jpg from subfolder
# __images__

# Then, it uses Gaussian blurring via the OpenCV library to
# smooth out noise for more accurate results. Then, it applies
# canny edge detection. Finally, we use the matplotlib library
# to display the result

# Required libraries, cv2, matplotlib


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_dir = os.path.join(script_dir, '__images__')

# Load the image
image = cv2.imread(os.path.join(file_dir, 'image1.jpg'))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 10, 100)

# Display the result
plt.imshow(edges, cmap='gray')
plt.show()
