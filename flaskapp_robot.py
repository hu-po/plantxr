import cv2
import numpy as np
from flask import Flask, send_from_directory, jsonify, Response

app = Flask(__name__, static_url_path='', static_folder='.')

def get_processed_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()  # Make sure to release the capture immediately after reading the frame

    if not ret:
        return None

    # Split the frame into left and right
    width = frame.shape[1]
    left_frame = frame[:, :width//2]
    right_frame = frame[:, width//2:]
    # Resize each half to 960x540
    left_resized = cv2.resize(left_frame, (960, 540))
    right_resized = cv2.resize(right_frame, (960, 540))
    # Combine them into a new frame
    combined_frame = np.vstack((left_resized, right_resized))

    # Convert the frame to a byte stream
    frame_bytes = cv2.imencode('.jpg', combined_frame)[1].tobytes()
    return frame_bytes

@app.route('/')
def index():
    return send_from_directory('.', 'flask_stereo.html')

@app.route('/api/image')
def serve_image():
    frame_bytes = get_processed_frame()
    if frame_bytes:
        return Response(frame_bytes, content_type='image/jpeg')
    else:
        return "Failed to capture frame", 500

@app.route('/api/servos')
def get_servo_angles():
    servos = np.random.uniform(-1, 1, size=3)
    return jsonify({'servos': servos.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
