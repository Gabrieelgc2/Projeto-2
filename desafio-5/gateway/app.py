from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://user-service:5001/servico"
ORDER_SERVICE = "http://order-service:5002/servico"

@app.route("/api/users", methods=["GET"])
def gateway_users():
    resp = requests.get(f"{USER_SERVICE}/users")
    return jsonify(resp.json())

@app.route("/api/orders/<int:user_id>", methods=["GET"])
def gateway_orders(user_id):
    resp = requests.get(f"{ORDER_SERVICE}/orders/{user_id}")
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
