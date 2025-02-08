from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, User, Project, Criterion
from backend.app import app

from backend.mcda.core.core import Pairwise

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from backend.app.routes.utils import save_project_in_session, delete_project_from_session

# from backend.mcda.core.core import Criterion

jwt = JWTManager(app)


@app.route("/api/save-criterion-to-db", methods=['POST'])
@jwt_required()
def save_criterion_to_db():
    post_data = request.get_json()
    criterion_name = post_data['name']
    criterion_beneficiality = post_data['beneficiality']
    criterion_description = post_data['description']
    task_id = post_data['taskID']
    values = post_data['values']
    pairwise = post_data['pairwise']

    if pairwise:
        pw = Pairwise(values)
        values = pw.calculate_eigenvector()

    # add criterion
    new_criterion = Criterion(criterion_name=criterion_name, min_max=criterion_beneficiality,
                              alternatives_values=values, description=criterion_description, task_id=task_id)
    sql_session.add(new_criterion)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Criterion not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Criterion Saved!", "criterion_id": new_criterion.criterion_id}

    return jsonify(response)


@app.route("/api/get-criteria-by-task-id", methods=['POST'])
@jwt_required()
def get_criteria_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']
    criteria = (
        sql_session
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


@app.route("/api/delete-criteria-by-id", methods=['POST'])
@jwt_required()
def delete_criteria_by_id():
    post_data = request.get_json()
    criteria_ids = post_data['criteriaIDs']

    for crit_id in criteria_ids:
        criterion = Criterion.query.get(crit_id)

        if criterion:
            sql_session.delete(criterion)

    response = {}
    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Criterion not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)
