from flask import Flask, Response, render_template
import cv2
import face_recognition
import pyttsx3
import os
import threading
import queue  # ✅ Queue for safe alert handling

app = Flask(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed
alert_queue = queue.Queue()  # ✅ Queue to handle alert messages safely

# Load known faces
project_dir = os.path.dirname(os.path.abspath(__file__)) 
known_faces_dir = os.path.join(project_dir, "images")

known_faces = []
known_labels = []

# Load face encodings
for filename in os.listdir(known_faces_dir):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(img_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:
            known_faces.append(encoding[0])
            known_labels.append(os.path.splitext(filename)[0])

# Initialize camera and lock
lock = threading.Lock()
camera = cv2.VideoCapture(0)

# ✅ Alert handling function in a separate thread
def alert_worker():
    """Continuously plays alert messages from the queue."""
    while True:
        message = alert_queue.get()
        print(f"🔔 Alert: {message}")
        engine.say(message)
        engine.runAndWait()
        alert_queue.task_done()

# Start the alert thread
alert_thread = threading.Thread(target=alert_worker, daemon=True)
alert_thread.start()


def generate_frames():
    """Video stream with face detection, recognition, and alerts"""
    while True:
        with lock:
            ret, frame = camera.read()

        if not ret:
            break

        # Convert the frame from BGR to RGB for face_recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_labels[first_match_index]
            else:
                # ✅ Add alert message to queue (no threading conflict)
                alert_queue.put("⚠️ Unknown person detected!")

            # Draw bounding boxes and labels
            top, right, bottom, left = face_location
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)  # Green for known, Red for unknown
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Encode the frame as JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """Web interface page"""
    return render_template('index.html')


@app.route('/video')
def video():
    """Video streaming route"""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
