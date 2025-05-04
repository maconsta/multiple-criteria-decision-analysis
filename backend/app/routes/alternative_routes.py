from flask import request, jsonify, session as flask_session
from datetime import timedelta

from backend.app.db.models import session as sql_session, User, Alternative, Criterion
from backend.app import app

from flask_jwt_extended import create_access_token, get_csrf_token, jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies

from backend.app.routes.utils import authorize_request

jwt = JWTManager(app)


@app.route("/api/save-alternative-to-db", methods=['POST'])
@jwt_required()
@authorize_request
def save_alternative_to_db():
    post_data = request.get_json()
    alternative_name = post_data['name']
    alternative_description = post_data['description']
    task_id = post_data['taskID']
    # project_id = post_data['projectID']

    new_alternative = Alternative(alternative_name=alternative_name,
                                  description=alternative_description, task_id=task_id)
    sql_session.add(new_alternative)

    criteria = Criterion.query.filter_by(task_id=task_id).order_by(Criterion.criterion_id).all()
    if len(criteria) > 0:
        for crit in criteria:
            if crit.alternatives_values:
                temp_alternatives_values = crit.alternatives_values[:]
                temp_alternatives_values.append(1) # append a dummy value
                crit.alternatives_values = temp_alternatives_values
            if crit.alternatives_values_raw:
                temp_alternatives_values_raw = crit.alternatives_values_raw[:]
                temp_alternatives_values_raw.append(1)  # append a dummy value
                crit.alternatives_values_raw = temp_alternatives_values_raw
            sql_session.add(crit)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Alternative not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Alternative Saved!", "alternative_id": new_alternative.alternative_id}

    return jsonify(response)


@app.route("/api/get-alternatives-by-task-id", methods=['POST'])
@jwt_required()
@authorize_request
def get_alternatives_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    alternatives = (
        sql_session
        .query(Alternative.task_id, Alternative.alternative_name, Alternative.alternative_id, Alternative.description,
               )
        .filter(Alternative.task_id == task_id)
        .order_by(Alternative.alternative_id)
        .all()
    )

    result = []
    for alt in alternatives:
        result.append(
            {"taskID": alt.task_id, "name": alt.alternative_name, "alternativeID": alt.alternative_id,
             "description": alt.description})

    return jsonify(result)


@app.route("/api/delete-alternatives-by-id", methods=['POST'])
@jwt_required()
@authorize_request
def delete_alternatives_by_id():
    post_data = request.get_json()
    alternatives_ids = post_data['alternativesIDs']
    task_id = post_data['taskID']

    alternatives = Alternative.query.filter_by(task_id=task_id).all()

    for index, alt in enumerate(alternatives):
        if alt.alternative_id in alternatives_ids:
            criteria = Criterion.query.filter_by(task_id=task_id).all()

            for crit in criteria:
                if crit.alternatives_values:
                    temp_alternatives_values = crit.alternatives_values[:]
                    temp_alternatives_values_raw = crit.alternatives_values_raw[:]
                    temp_alternatives_values.pop(index)
                    temp_alternatives_values_raw.pop(index)
                    crit.alternatives_values = temp_alternatives_values
                    crit.alternatives_values_raw = temp_alternatives_values_raw
                    sql_session.add(crit)

            sql_session.delete(alt)

    response = {}
    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Alternatives not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)

