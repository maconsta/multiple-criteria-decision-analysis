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
@app.route("/save-criterion-to-db", methods=['POST'])
def save_criterion_to_db():
    post_data = request.get_json()
    criterion_name = post_data['name']
    criterion_beneficiality = post_data['beneficiality']
    criterion_description = post_data['description']
    task_id = post_data['taskID']

    new_criterion = Criterion(criterion_name=criterion_name, min_max=criterion_beneficiality,
                              description=criterion_description, task_id=task_id)
    session.add(new_criterion)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Criterion not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Criterion Saved!", "criterion_id": new_criterion.criterion_id}

    return jsonify(response)


@app.route("/get-criteria-by-task-id", methods=['POST'])
def get_criteria_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    criteria = (
        session
        .query(Criterion.task_id, Criterion.criterion_name, Criterion.criterion_id, Criterion.description,
               Criterion.min_max)
        .filter(Criterion.task_id == task_id)
        .all()
    )

    result = []
    for crit in criteria:
        result.append(
            {"taskID": crit.task_id, "name": crit.criterion_name, "criterionID": crit.criterion_id,
             "description": crit.description, "beneficiality": crit.min_max})

    return jsonify(result)


@app.route("/delete-criteria-by-id", methods=['POST'])
def delete_criteria_by_id():
    post_data = request.get_json()
    criteria_ids = post_data['criteriaIDs']

    for crit_id in criteria_ids:
        criterion = Criterion.query.get(crit_id)

        if criterion:
            session.delete(criterion)

    response = {}
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Criterion not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)


@app.route("/calculate-results", methods=['POST'])
def calculate_results():
    post_data = request.get_json()
    weight_matrix_raw = post_data['weightMatrix']
    alternatives_raw = post_data['alternatives']
    criteria_raw = post_data['criteria']

    # print(weight_matrix_raw)
    # print(alternatives_raw)
    # print(criteria_raw)

    criteria = []
    for crit in criteria_raw:
        c = Crit(name=crit['name'], min_max=crit['beneficiality'])
        criteria.append(c)

    alternatives = []
    # for alt in alternatives_raw:
    # alternatives need values, fix that first and come back
    # a = Alt()

    # print(criteria)

    return jsonify("test")



