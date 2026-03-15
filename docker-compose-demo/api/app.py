import os
import time
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_NAME = os.environ.get("POSTGRES_DB", "postgres")
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "secret")

@app.route("/")
def root():
    return "API service is running. Use /users"

@app.route("/users")
def users():
    for _ in range(10):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                connect_timeout=3,
            )
            break
        except Exception:
            time.sleep(1)
    else:
        return jsonify({"error": "could not connect to database"}), 500

    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);")
            cur.execute("INSERT INTO users (name) VALUES ('alice');")
            cur.execute("SELECT id, name FROM users LIMIT 5;")
            rows = cur.fetchall()

    return jsonify({"users": [{"id": r[0], "name": r[1]} for r in rows]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
