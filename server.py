from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data["msg"])
    return {"status": "ok"}

@app.route("/get", methods=["GET"])
def get():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)