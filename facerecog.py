import cv2
import numpy as np
import os
import pyttsx3  # For voice alerts (optional)
import face_recognition  # For face recognition

# Initialize text-to-speech engine (optional for alerts)
engine = pyttsx3.init()

# Specify the directory containing known faces
project_dir = os.path.dirname(os.path.abspath(__file__))  # Get current project directory
known_faces_dir = os.path.join(project_dir, "images")

# Load known faces and their labels
known_faces = []
known_labels = []

for filename in os.listdir(known_faces_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):  # Ensure it's an image file
        img_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)
        if encoding:  # Check if encoding was found
            known_faces.append(encoding[0])
            known_labels.append(os.path.splitext(filename)[0])  # Use filename (without extension) as label

# Initialize the video capture (use 0 for webcam)
camera = cv2.VideoCapture(0)

# Define minimum confidence threshold for object detection
CONFIDENCE_THRESHOLD = 0.5

def alert_user(message):
    """Send an alert (optional: speech alert)."""
    print(message)
    engine.say(message)  # Speak the message out loud
    engine.runAndWait()

while True:
    # Capture frame from the camera
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture video")
        break

    # Convert the frame from BGR to RGB for face_recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop over the detected face encodings
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # If a match was found, find the corresponding label
        if True in matches:
            first_match_index = matches.index(True)
            name = known_labels[first_match_index]

        # Draw a rectangle around the detected face
        (top, right, bottom, left) = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Trigger an alert if an unknown person is detected
        if name == "Unknown":
            alert_user("Alert! Unknown person detected!")

    # Show the output frame
    cv2.imshow("AI Surveillance Camera", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
