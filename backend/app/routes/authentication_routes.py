import os, hashlib

from flask import request, jsonify, session as flask_session
from datetime import timedelta

from backend.app.db.models import session, User
from backend.app import app

from flask_jwt_extended import (
    create_access_token,
    get_csrf_token,
    get_jwt_identity,
    verify_jwt_in_request,
    unset_jwt_cookies, jwt_required,
)
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies

jwt = JWTManager(app)


def hash_password(password: str):
    # Create a 16-byte salt
    salt = os.urandom(16)

    # Hash the password with the salt
    hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)

    # Return the salt and hashed password combined, both encoded as hex
    return salt.hex() + hashed_password.hex()


def verify_password(stored_password: str, provided_password: str):
    # Extract the salt from the first 32 characters (16 bytes in hex form)
    salt = bytes.fromhex(stored_password[:32])

    # Extract the hashed password
    stored_hashed_password = stored_password[32:]

    # Hash the provided password using the extracted salt
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", provided_password.encode(), salt, 100000
    )

    # Convert hashed password to hex for comparison
    hashed_password_hex = hashed_password.hex()

    # Compare the stored hashed password with the newly hashed password
    return hashed_password_hex == stored_hashed_password


@app.route("/api/register-user", methods=["POST"])
def register_user():
    post_data = request.get_json()
    firstName = post_data["firstName"]
    lastName = post_data["lastName"]
    email = post_data["email"]
    password = post_data["password"]

    # hash the password using hashlib
    hashed_password = hash_password(password)

    new_user = User(
        first_name=firstName, last_name=lastName, email=email, password=hashed_password
    )

    session.add(new_user)

    response = {}

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {
            "result": "User not registered, error: " + str(e) + "!",
            "success": False,
        }
    else:
        token = create_access_token(
            identity=str(new_user.user_id), expires_delta=timedelta(weeks=1)
        )

        response = jsonify(
            {
                "result": "User registered!",
                "userID": new_user.user_id,
                "success": True,
                "csrfToken": get_csrf_token(token),
            }
        )

        # projects = flask_session.get("projects")
        # if projects is not None:
        #     projects.clear()

        set_access_cookies(response, token)

    return response


@app.route("/api/sign-in", methods=["POST"])
def sign_in():
    post_data = request.get_json()
    email = post_data["email"]
    password = post_data["password"]

    user = session.query(User).filter_by(email=email).first()
    if user and verify_password(user.password, password):
        token = create_access_token(
            identity=str(user.user_id), expires_delta=timedelta(weeks=1)
        )

        response = jsonify({
            "result": "User signed in!",
            "userID": user.user_id,
            "success": True,
            "csrfToken": get_csrf_token(token),
        })
        
        set_access_cookies(response, token)
    else:
        response = jsonify({"result": "Invalid email or password", "success": False})

    return response


@app.route("/api/is-logged-in", methods=["GET"])
def is_logged_in():
    token = verify_jwt_in_request(optional=True)

    if token:
        response = {"success": True}
    else:
        response = {"success": False, "result": "Token not present"}

    return response

@app.route("/sign-out", methods=["GET"])
def sign_out():
    response = jsonify({"result": "User signed out!", "success": True})

    # flask_session.get("projects").clear()
    # flask_session.modified = True

    unset_jwt_cookies(response)

    return response

@app.route("/api/get-user-abbreviation", methods=["GET"])
@jwt_required()
def get_user_abbreviation():
    user_id = get_jwt_identity()
    user = session.query(User).filter_by(user_id=user_id).first()

    abbr = user.first_name[0] + user.last_name[0]

    result = {"success": True, "abbreviation": abbr.upper()}

    return result