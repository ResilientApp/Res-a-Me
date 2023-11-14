from localDatabase import getLoginInfo, getUserInfo
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = getLoginInfo(username)
        if user and user['password'] == password:
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    else:
        return jsonify({"message": "Username and password are required"}), 400

@app.route('/get_user_data/<username>', methods=['GET'])
def get_user_data(username):
    user = getUserInfo(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port = 3033)
