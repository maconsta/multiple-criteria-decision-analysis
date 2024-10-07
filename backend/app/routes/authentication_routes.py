from flask import request, jsonify, session as flask_session
from datetime import timedelta

from backend.app.db.models import session, User
from backend.app import app

from flask_jwt_extended import create_access_token, get_csrf_token, get_jwt_identity, verify_jwt_in_request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies

jwt = JWTManager(app)


@app.route("/register-user", methods=['POST'])
def register_user():
    post_data = request.get_json()
    firstName = post_data['firstName']
    lastName = post_data['lastName']
    email = post_data['email']
    password = post_data['password']

    new_user = User(first_name=firstName, last_name=lastName, email=email, password=password)

    session.add(new_user)

    response = {}

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "User not registered, error: " + str(e) + "!", "success": False}
    else:
        token = create_access_token(identity=str(new_user.user_id), expires_delta=timedelta(weeks=1))

        response = jsonify({"result": "User registered!", "userID": new_user.user_id, "success": True,
                            "csrf_token": get_csrf_token(token)})

        projects = flask_session.get("projects")
        if projects is not None:
            projects.clear()

        set_access_cookies(response, token)

    return response


@app.route("/is-logged-in", methods=['GET'])
def is_logged_in():
    token = verify_jwt_in_request(optional=True)

    if token:
        response = {"success": True}
    else:
        response = {"success": False, "result": "Token not present"}

    return response