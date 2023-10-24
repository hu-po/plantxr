import cv2
import numpy as np
from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='', static_folder='.')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def gen_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
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
        # Send the byte stream over the WebSocket connection
        yield frame_bytes
    cap.release()

# Serve your main WebXR HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'flask_stereo.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

@socketio.on('stream_request')
def on_stream_request():
    print('Stream requested')
    # Send the decoded video stream over the WebSocket connection
    for frame in gen_frames():
        emit('stream_frame', {'data': frame})

if __name__ == '__main__':
    socketio.run(app, debug=True)
