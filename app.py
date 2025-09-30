from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Route mặc định để kiểm tra server
@app.route('/')
def home():
    return "Flask app running for Zalo OA integration!"

# Route phục vụ file xác minh Zalo (tĩnh)
@app.route('/<path:filename>')
def serve_verifier(filename):
    # Tìm file trong thư mục hiện tại (repo root)
    return send_from_directory('.', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
