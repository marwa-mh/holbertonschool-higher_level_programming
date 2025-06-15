#!/usr/bin/python3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username: str):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 400

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.get_json() is None:
        abort(400, "Not a JSON")
    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400
    
    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }

    output = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    return jsonify({"message":"user added", "user": output}), 201


if __name__ == "__main__":
    app.run()
