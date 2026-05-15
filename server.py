from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# stocke les connexions
connections = []

@app.route("/")
def home():
    return "Serveur OK 🚀"

# appelé par le client quand il se connecte
@app.route("/connect")
def connect():
    ip = request.remote_addr

    connections.append({
        "ip": ip,
        "time": time.time()
    })

    print(f"🟢 Connexion: {ip}")

    return {"status": "connected"}

# status pour ton client Python
@app.route("/status")
def status():
    now = time.time()

    # garder seulement les connexions des 30 dernières secondes
    active = [c for c in connections if now - c["time"] < 30]

    return jsonify({
        "online": len(active),
        "clients": active
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
