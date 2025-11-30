from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Gabriel"},
    {"id": 2, "name": "Fernando"},
    {"id": 3, "name": "João"}
]

@app.route("/servico/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/servico/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for u in users:
        if u["id"] == user_id:
            return jsonify(u)
    return jsonify({"error": "Usuário não existe"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
