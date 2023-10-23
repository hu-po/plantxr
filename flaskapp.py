from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

# Serve your main WebXR HTML file
@app.route('/')
def index():
    return send_from_directory('static', 'webxr.html')

# API endpoint for Python processing
@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Your Python logic here
    return {"result": "analysis result"}

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # This runs the Flask server with an ad-hoc SSL context for HTTPS
