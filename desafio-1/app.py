from flask import Flask, request, jsonify
import redis
import os
import sqlite3
app = Flask(__name__)

db_path = os.getenv("SQLITE_PATH", "/data/sqlite/mydb.sqlite3") # Caminho do banco de dados SQLITE

os.makedirs("/data/sqlite", exist_ok=True) # Criação do diretório para o banco de dados SQLITE

def init_db(): # Criação do banco de dados SQLITE
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

init_db()


def get_connection(): # Função para conectar ao banco de dados SQLITE
    return sqlite3.connect(db_path)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/set", methods=["POST"]) # Redis
def set_value():
    data = request.get_json()
    r.set(data["key"], data["value"])
    return jsonify({"message": "Valor salvo com sucesso!"})

@app.route("/get/<key>", methods=["GET"]) # Redis
def get_value(key):
    value = r.get(key)
    if value:
        return jsonify({"key": key, "value": value})
    return jsonify({"error": "Chave não encontrada"}), 404

@app.route("/add_user/<nome>", methods=["POST"]) # SQLITE
def add_user(nome):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Usuário salvo!", "nome": nome})

@app.route("/users", methods=["GET"]) # SQLITE
def list_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)