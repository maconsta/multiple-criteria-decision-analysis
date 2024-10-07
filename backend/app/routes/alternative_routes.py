from flask import request, jsonify, session as flask_session
from datetime import timedelta

from backend.app.db.models import session, User, Alternative
from backend.app.routes.utils import save_alt_in_session
from backend.app import app

from flask_jwt_extended import create_access_token, get_csrf_token, jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies

jwt = JWTManager(app)


@app.route("/save-alternative-to-db", methods=['POST'])
@jwt_required()
def save_alternative_to_db():
    post_data = request.get_json()
    alternative_name = post_data['name']
    alternative_description = post_data['description']
    task_id = post_data['taskID']

    new_alternative = Alternative(alternative_name=alternative_name,
                                  description=alternative_description, task_id=task_id)
    session.add(new_alternative)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Alternative not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Alternative Saved!", "alternative_id": new_alternative.alternative_id}
        save_alt_in_session()

    return jsonify(response)


@app.route("/get-alternatives-by-task-id", methods=['POST'])
def get_alternatives_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    alternatives = (
        session
        .query(Alternative.task_id, Alternative.alternative_name, Alternative.alternative_id, Alternative.description,
               )
        .filter(Alternative.task_id == task_id)
        .all()
    )

    result = []
    for alt in alternatives:
        result.append(
            {"taskID": alt.task_id, "name": alt.alternative_name, "alternativeID": alt.alternative_id,
             "description": alt.description})

    return jsonify(result)


@app.route("/delete-alternatives-by-id", methods=['POST'])
def delete_alternatives_by_id():
    post_data = request.get_json()
    alternatives_ids = post_data['alternativesIDs']

    for alt_id in alternatives_ids:
        alt = Alternative.query.get(alt_id)

        if alt:
            session.delete(alt)

    response = {}
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Alternatives not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)

