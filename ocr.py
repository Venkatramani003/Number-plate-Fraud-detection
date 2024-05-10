import cv2
import pytesseract

def image_to_text(image):
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('Frame', frame)

    # Convert the frame to grayscale for OCR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Call the function to perform OCR
    text = image_to_text(gray)
    print("Detected Text:", text)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
