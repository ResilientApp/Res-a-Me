from controller import getUserLogin, seUserLogin, getUserInfo, setUserInfo
from flask import Flask, request, jsonify, session, url_for
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager

from flask_cors import CORS

from flask_session import Session
from datetime import timedelta

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=30)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(seconds=60)
jwt = JWTManager(app)

CORS(app, supports_credentials=True)


# parse user register request and store in database
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email and password:
        user = getUserLogin(email)
        if not user:
            seUserLogin(email, password)
            return jsonify({"message": "Register successful"}, status = 200)
        else:
            return jsonify({"message": "email account existed"}, status = 401)
    else:
        return jsonify({"message": "email and password are required"}, status = 400)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}, status = 401)

    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)  # Create a refresh token
    return jsonify(access_token=access_token, refresh_token=refresh_token, status = 200)


@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token, status = 200)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/loadUser", methods=["GET"])
@jwt_required()
def load_logged_in_user():
    print(jwt)
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user, status = 200)
    else:
        return jsonify(status = 401)


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()

#     email = data.get('email')
#     password = data.get('password')

#     print(email, password)

#     if session:
#         # already logged in
#         print(session["email"], session["password"], "Already Logged In")
#         return url_for('/')
#     else:
#         if email and password:
#             user = getUserLogin(email)
#             if user and user['password'] == password:
#                 session["email"] = email
#                 session["username"] = user
#                 session["password"] = password
                
#                 return jsonify({"message": "Login successful"})
#             else:
#                 return jsonify({"message": "Invalid email or password"}), 401
#         else:
#             return jsonify({"message": "email and password are required"}), 400
    
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()

#     email = data.get('email')
#     password = data.get('password')

#     if email and password:
#         user = getUserLogin(email)
#         if not user:
#             seUserLogin(email, password)
#             return jsonify({"message": "Register successful"})
#         else:
#             return jsonify({"message": "email account existed"}), 401
#     else:
#         return jsonify({"message": "email and password are required"}), 400
    
@app.route('/logout', methods=["GET"])
def logout():
    print("Logout")
    # session.clear()
    return jsonify({"message": "Logout successful"})


# @app.route('/get_user_data/<email>', methods=['GET'])
# def get_user_data(username):
#     user = getUserInfo(username)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port = 3033)
