import cv2
import numpy as np
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def gen_frames():
    cap = cv2.VideoCapture('media/video/bbb-sunflower-540p2-1min.webm')
    while True:
        success, frame = cap.read()
        if not success:
            break
        # Convert the frame to a byte stream
        frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        # Send the byte stream over the WebSocket connection
        yield frame_bytes
    cap.release()

@app.route('/')
def index():
    return render_template('flask_stereo.html')

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