from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = [
    {"user_id": 1, "order": "Mouse"},
    {"user_id": 1, "order": "Teclado"},
    {"user_id": 2, "order": "Monitor"}
]

USER_SERVICE_URL = "http://user-service:5001"

@app.route("/servico/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    resp = requests.get(f"{USER_SERVICE_URL}/servico/users/{user_id}")

    if resp.status_code != 200:
        return jsonify({"error": "Usuário não existe"}), 404

    user_orders = [o for o in orders if o["user_id"] == user_id]
    return jsonify(user_orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)