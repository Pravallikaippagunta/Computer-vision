import cv2
# Initialize the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    # Applying Gaussian blur with a larger kernel size
    gaussian_blur = cv2.GaussianBlur(frame, (51, 51), 0)  # Kernel size
    # Creating a canvas to display the original and blurred images
    canvas = cv2.hconcat([frame, gaussian_blur])  # Original and Gaussian blurred image
    # Displaying the original and blurred images
    cv2.imshow('Original and Blurred Image', canvas)
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
