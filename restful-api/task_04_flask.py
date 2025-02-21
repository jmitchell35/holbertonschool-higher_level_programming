#!/usr/bin/env python3
from flask import Flask, jsonify, request
import json
from markupsafe import escape

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<string:username>")
def username(username):
    if users[escape(username)]:
        return jsonify(users[escape(username)])
    else:
        return jsonify({"error": "Username is required"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    new_user = {
        data.get('username'): {
            key: value for key, value in data.items() if key != "username"}}
    users.update(new_user)

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)