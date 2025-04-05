from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, User, Project, Criterion, TradeOff
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
    criterion_type = post_data['critType']
    task_id = post_data['taskID']
    values = post_data['values']
    pairwise = post_data['pairwise']

    criterion_id = post_data['criterionID']

    values = [float(value) for value in values]
    raw_values = values

    if pairwise:
        pw = Pairwise(values)
        values = pw.calculate_eigenvector()

    if criterion_id:
        new_criterion = Criterion.query.filter_by(criterion_id=criterion_id).first()
        new_criterion.name = criterion_name
        new_criterion.beneficiality = criterion_beneficiality
        new_criterion.description = criterion_description
        new_criterion.criterion_type = criterion_type
        new_criterion.alternatives_values = values
        new_criterion.alternatives_values_raw = raw_values
    else:
        new_criterion = Criterion(criterion_name=criterion_name, min_max=criterion_beneficiality,
                                  alternatives_values=values, description=criterion_description, task_id=task_id,
                                  criterion_type=criterion_type, alternatives_values_raw=raw_values)

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
        .order_by(Criterion.criterion_id)
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
    task_id = post_data['taskID']

    criteria = Criterion.query.filter_by(task_id=task_id).all()

    for index, crit in enumerate(criteria):
        if crit.criterion_id in criteria_ids:
            trade_off = TradeOff.query.filter_by(task_id=task_id).first()  # always only one tradeoff

            cnt = 0
            indexes_to_remove = []
            for i in range(len(criteria) - 1):
                for j in range(i + 1, len(criteria)):
                    if i == index or j == index:
                        indexes_to_remove.append(cnt)
                    cnt += 1

            temp_criteria_weights_raw = [item for i, item in enumerate(trade_off.criteria_weights_raw[:]) if
                                         i not in indexes_to_remove]

            trade_off.criteria_weights_raw = temp_criteria_weights_raw
            pw = Pairwise(temp_criteria_weights_raw)
            new_criteria_weights = pw.calculate_eigenvector()
            trade_off.criteria_weights = new_criteria_weights

            sql_session.add(trade_off)
            sql_session.delete(crit)

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


@app.route("/api/get-criterion-info", methods=['POST'])
@jwt_required()
def get_criterion_info():
    post_data = request.get_json()
    criterion_id = post_data['criterionID']

    criterion = Criterion.query.filter_by(criterion_id=criterion_id).first()

    if criterion:
        result = {"name": criterion.criterion_name,
                  "description": criterion.description, "beneficiality": criterion.min_max,
                  "alternatives_values": [float(value) for value in criterion.alternatives_values],
                  "criterion_type": criterion.criterion_type,
                  "alternatives_values_raw": [float(value) for value in criterion.alternatives_values_raw]}
        status_code = 200
    else:
        result = {"result": "Catastrophic failure!"}
        status_code = 400

    return jsonify(result), status_code
