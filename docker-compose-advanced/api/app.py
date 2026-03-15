import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST','db')
DB_PORT = int(os.getenv('DB_PORT','5432'))
DB_NAME = os.getenv('POSTGRES_DB','demo')
DB_USER = os.getenv('POSTGRES_USER','demo')
DB_PASS = os.getenv('POSTGRES_PASSWORD','secret')

@app.route('/health')
def health():
    return 'ok'

@app.route('/users')
def users():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    with conn:
        with conn.cursor() as cur:
            cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT);')
            cur.execute("INSERT INTO users (name) VALUES ('alice')")
            cur.execute('SELECT id, name FROM users;')
            rows = cur.fetchall()
    return jsonify([{'id': r[0], 'name': r[1]} for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
