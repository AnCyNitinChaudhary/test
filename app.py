import cv2

def capture_image():
    # Open the default camera (usually the first one)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the camera")
        return

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame")
        return

    # Release the camera
    cap.release()

    # Save the captured frame as an image
    cv2.imwrite("captured_image.jpg", frame)

    # Display the captured image
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
