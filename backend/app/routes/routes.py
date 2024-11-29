from flask import render_template, request, jsonify, session as flask_session
from datetime import datetime, timedelta

from backend.app.db.models import session, User, Project, Task, Criterion, Alternative
from backend.mcda.core.core import Criterion as Crit, Alternative as Alt
from backend.app import app

from flask_jwt_extended import create_access_token, get_csrf_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies

jwt = JWTManager(app)

# TODO: cleanup here

@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, world!")


# TODO: add jwt_required decorator and fix routes logic

#
# @app.route("/calculate-results", methods=['POST'])
# def calculate_results():
#     post_data = request.get_json()
#     weight_matrix_raw = post_data['weightMatrix']
#     alternatives_raw = post_data['alternatives']
#     criteria_raw = post_data['criteria']
#
#     # print(weight_matrix_raw)
#     # print(alternatives_raw)
#     # print(criteria_raw)
#
#     criteria = []
#     for crit in criteria_raw:
#         c = Crit(name=crit['name'], min_max=crit['beneficiality'])
#         criteria.append(c)
#
#     alternatives = []
#     # for alt in alternatives_raw:
#     # alternatives need values, fix that first and come back
#     # a = Alt()
#
#     # print(criteria)
#
#     return jsonify("test")
#
#

