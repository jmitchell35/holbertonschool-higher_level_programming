#!/usr/bin/env python3
from flask import Flask, jsonify, request
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
    req_username = escape(username)
    req_user = {"username" : req_username}
    if req_username in users:
        req_user.update(
            {key: value for key, value in users[req_username].items()}
            )
        return jsonify(req_user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    new_user = {
        data.get('username'): {
            key: value for key, value in data.items() if key != "username"}}
    users.update(new_user)

    return jsonify({
        "message": "User added",
        "user": data
        }
    ), 201

if __name__ == '__main__':
    app.run(debug=True)