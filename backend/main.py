import os
from controller import getUserLogin, setUserLogin, getUserInfo, setUserInfo
from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=30)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(seconds=60)
jwt = JWTManager(app)


# Setup the image upload folder
app.config['UPLOAD_FOLDER'] = "../frontend/public/images/pictures"

CORS(app, supports_credentials=True)


# parse user register's request and store in database
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email and password:
        user = getUserLogin(email)
        if not user:
            setUserLogin(email, password)
            return jsonify(message = "Register successful", status = 200)
        else:
            return jsonify(message = "email account existed", status = 401)
    else:
        return jsonify(message = "email and password are required", status = 400)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email and password:
        user = getUserLogin(email)
        if user and user['password'] == password:               
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            return jsonify(access_token=access_token, refresh_token=refresh_token, status = 200)
        else:
            return jsonify(message = "Invalid email or password", status = 401)
    else:
        return jsonify(message = "email and password are required", status = 400)


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
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user, status = 200)
    else:
        return jsonify(status = 401)

    
@app.route('/logout', methods=["GET"])
def logout():
    print("Logout")
    # session.clear()
    return jsonify(message = "Logout successful", status = 200)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/upload', methods=['POST'])
def upload():
    print("Upload")
    
    if 'image' not in request.files:
        return jsonify(message = "No file part", status=400)

    file = request.files['image']
    print(file)

    if file.filename == '':
        return jsonify(message = "No selected file", status=400)

    if file and allowed_file(file.filename):
        filename = "avatar.png"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(file_path)
        file.save(file_path)
        return jsonify(message="Upload successful", status=200, path=file_path)

    return jsonify(message="File type not allowed", status=400)



# @app.route('/get_user_data/<email>', methods=['GET'])
# def get_user_data(username):
#     user = getUserInfo(username)
#     if user:
#         return jsonify(user)
#     else:
#         return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port = 3033)
