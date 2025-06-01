import os, hashlib
from datetime import timedelta
from flask import request, jsonify
from backend.app import app
from backend.app.db.models import session_scope, User
from flask_jwt_extended import (
    create_access_token,
    verify_jwt_in_request,
    JWTManager,
)

jwt = JWTManager(app)


def hash_password(password: str):
    # Create a 16-byte salt.
    salt = os.urandom(16)
    # Hash the password with the salt.
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    # Return the salt and hashed password combined both encoded as hex
    return salt.hex() + hashed_password.hex()


def verify_password(stored_password: str, provided_password: str):
    # Extract the salt from the first 32 characters (16 bytes in hex)
    salt = bytes.fromhex(stored_password[:32])
    # Extract the stored hashed password
    stored_hashed_password = stored_password[32:]
    # Hash the provided password using the same salt.
    hashed_password = hashlib.pbkdf2_hmac("sha256", provided_password.encode(), salt, 100000)
    # Compare the stored hashed password with the computed hash.
    return hashed_password.hex() == stored_hashed_password


@app.route("/api/register-user", methods=["POST"])
def register_user():
    try:
        with session_scope() as db:
            post_data = request.get_json()
            firstName = post_data["firstName"]
            lastName = post_data["lastName"]
            email = post_data["email"]
            password = post_data["password"]

            # Hash the password.
            hashed_password = hash_password(password)

            # Create a new User instance.
            new_user = User(
                first_name=firstName,
                last_name=lastName,
                email=email,
                password=hashed_password,
            )


            db.add(new_user)
            db.flush()

            access_token = create_access_token(
                identity=str(new_user.user_id), expires_delta=timedelta(days=1)
            )
            response = jsonify({
                "result": "User registered!",
                "userID": new_user.user_id,
                "success": True,
                "accessToken": access_token,
            })
    except Exception as e:
        response = jsonify({
            "result": "User not registered, error: " + str(e) + "!",
            "success": False,
        })
    return response


@app.route("/api/sign-in", methods=["POST"])
def sign_in():
    try:
        post_data = request.get_json()
        email = post_data["email"]
        password = post_data["password"]

        with session_scope() as db:
            user = db.query(User).filter_by(email=email).first()
            if user:
                stored_password = user.password
                user_id = user.user_id
            else:
                stored_password = None
                user_id = None

        if user and verify_password(stored_password, password):
            access_token = create_access_token(
                identity=str(user_id), expires_delta=timedelta(days=1)
            )
            response = jsonify({
                "result": "User signed in!",
                "userID": user_id,
                "success": True,
                "accessToken": access_token,
            })
        else:
            response = jsonify({
                "result": "Invalid email or password",
                "success": False,
            })
    except Exception as e:
        response = jsonify({
            "result": "Sign in failed, error: " + str(e),
            "success": False,
        })
        return response, 500
    return response


@app.route("/api/is-logged-in", methods=["GET"])
def is_logged_in():
    try:
        token = verify_jwt_in_request(optional=True)
        if token:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "result": "Token not present"})
    except Exception as e:
        return jsonify({"success": False, "result": str(e)}), 500


@app.route("/api/sign-out", methods=["GET"])
def sign_out():
    response = jsonify({"result": "User signed out!", "success": True})
    return response
