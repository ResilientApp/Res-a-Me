from controller import getUserLogin, seUserLogin, getUserInfo, setUserInfo
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if email and password:
        user = getUserLogin(email)
        if user and user['password'] == password:
            return jsonify({"message": "Login successful"})
        else:
            return jsonify({"message": "Invalid email or password"}), 401
    else:
        return jsonify({"message": "email and password are required"}), 400
    
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if email and password:
        user = getUserLogin(email)
        if not user:
            seUserLogin(email, password)
            return jsonify({"message": "Register successful"})
        else:
            return jsonify({"message": "email account existed"}), 401
    else:
        return jsonify({"message": "email and password are required"}), 400


# @app.route('/get_user_data/<email>', methods=['GET'])
# def get_user_data(username):
#     user = getUserInfo(username)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port = 3033)
