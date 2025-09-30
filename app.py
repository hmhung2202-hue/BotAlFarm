from flask import Flask, send_from_directory

app = Flask(__name__)

# Route mặc định để test
@app.route('/')
def home():
    return "Flask app running for Zalo OA integration!"

# Route phục vụ file xác minh
@app.route('/<filename>')
def verify(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
