from flask import Flask, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__, static_url_path='', static_folder='.')

# Serve your main WebXR HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'flask_stereo.html')

# API endpoint for Python processing
@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Your Python logic here
    return {"result": "analysis result"}

@app.route('/api/current_time', methods=['GET'])
def current_time():
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_time": time_string})

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # This runs the Flask server with an ad-hoc SSL context for HTTPS