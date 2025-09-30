from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app running for Zalo OA integration!"

# Route cho xác thực domain với Zalo
@app.route('/zalo_verifierPTsW5Q-f325ke9Hyjw...KSDJOq.html')
def verify():
    return "zalo_verifierPTsW5Q-f325ke9Hyjw...KSDJOq.html"

# Webhook để nhận sự kiện từ Zalo OA
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook data:", data)
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
