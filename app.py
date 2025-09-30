from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app running for Zalo OA integration!"

# Route để phục vụ file xác minh Zalo
@app.route('/<path:filename>')
def verify_file(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
