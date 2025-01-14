# Your task for today is to make a program that starts the computer camera and
# detects moving objects. The camera view draws a rectangle near the region where
# an object entered the camera.

# We use the opencv library for this. Below you will find a simple script to get
# you started. The script starts the camera, converts the frames into grayscale,
# and shows a grayscale live video.

import cv2

# Initialize the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Read the first frame to initialize the background
ret, frame = cap.read()
if not ret:
    print("Failed to grab frame")
    exit()

# Convert the frame to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale frame
gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

# Initialize the background
background = gray_frame

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()
    
    # If frame is read correctly, ret is True
    if not ret:
        print("Failed to grab frame")
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale frame
    gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)
    
    # Compute the absolute difference between the current frame and the background
    diff_frame = cv2.absdiff(background, gray_frame)
    
    # Apply a threshold to the difference frame
    _, thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)
    
    # Dilate the threshold frame to fill in holes
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    # Find contours in the threshold frame
    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around the contours
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Motion Detection', frame)
    
    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()