import json
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

@app.route('/load/<user_id>', methods=['GET'])
def load_resume(user_id):
    try:
        with open(f'resumes/{user_id}.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"message": "Resume not found"}), 404

@app.route('/edit/<user_id>', methods=['POST'])
def edit_resume(user_id):
    data = request.get_json()

    if data is None:
        return jsonify({"message": "No data provided"}), 400

    try:
        with open(f'resumes/{user_id}.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify({"message": "Resume updated successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500
        

# @app.route('/get_user_data/<email>', methods=['GET'])
# def get_user_data(username):
#     user = getUserInfo(username)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port = 3033)
