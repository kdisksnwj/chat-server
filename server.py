from flask import Flask, request, jsonify
import time

app = Flask(__name__)

connections = {}

@app.route("/")
def home():
    return "Serveur OK 🚀"

# le client appelle ça quand il se connecte
@app.route("/connect")
def connect():
    ip = request.remote_addr
    connections[ip] = time.time()
    return {"status": "connected"}

# GitHub Pages va lire ça
@app.route("/status")
def status():
    now = time.time()

    # garder seulement les connexions des 30 dernières sec
    active = {ip: t for ip, t in connections.items() if now - t < 30}

    return jsonify({
        "online": len(active),
        "clients": list(active.keys())
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
