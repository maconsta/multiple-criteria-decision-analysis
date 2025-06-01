from flask import request, jsonify
from backend.app.db.models import session_scope, Criterion, TradeOff
from backend.app import app
from backend.app.routes.utils import authorize_request
from backend.mcda.core.core import Pairwise
from flask_jwt_extended import jwt_required, JWTManager

jwt = JWTManager(app)


@app.route("/api/save-criterion-to-db", methods=['POST'])
@jwt_required()
@authorize_request
def save_criterion_to_db():
    post_data = request.get_json()
    criterion_name = post_data['name']
    criterion_beneficiality = post_data['beneficiality']
    criterion_description = post_data['description']
    criterion_type = post_data['critType']
    task_id = post_data['taskID']
    values = post_data['values']
    pairwise = post_data['pairwise']

    criterion_id = post_data.get('criterionID')

    values = [float(value) for value in values]
    raw_values = values[:]

    if pairwise:
        pw = Pairwise(values)
        values = pw.calculate_eigenvector()

    try:
        with session_scope() as db:
            if criterion_id:
                criterion_obj = db.query(Criterion).filter_by(criterion_id=criterion_id).first()
                if not criterion_obj:
                    return jsonify({"result": "Criterion not found!"}), 404
                criterion_obj.criterion_name = criterion_name
                criterion_obj.min_max = criterion_beneficiality
                criterion_obj.description = criterion_description
                criterion_obj.criterion_type = criterion_type
                criterion_obj.alternatives_values = values
                criterion_obj.alternatives_values_raw = raw_values
                db.add(criterion_obj)
                new_criterion = criterion_obj
            else:
                new_criterion = Criterion(
                    criterion_name=criterion_name,
                    min_max=criterion_beneficiality,
                    alternatives_values=values,
                    description=criterion_description,
                    task_id=task_id,
                    criterion_type=criterion_type,
                    alternatives_values_raw=raw_values
                )
                db.add(new_criterion)
        response = {"result": "Criterion Saved!", "criterion_id": new_criterion.criterion_id}
    except Exception as e:
        response = {"result": "Criterion not saved, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/get-criteria-by-task-id", methods=['POST'])
@jwt_required()
@authorize_request
def get_criteria_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    try:
        with session_scope() as db:
            criteria = (
                db.query(
                    Criterion.task_id,
                    Criterion.criterion_name,
                    Criterion.criterion_id,
                    Criterion.description,
                    Criterion.min_max,
                    Criterion.alternatives_values_raw,
                    Criterion.preference_function,
                    Criterion.p_value,
                    Criterion.q_value
                )
                .filter(Criterion.task_id == task_id)
                .order_by(Criterion.criterion_id)
                .all()
            )
        result = []
        for crit in criteria:
            result.append({
                "taskID": crit.task_id,
                "name": crit.criterion_name,
                "criterionID": crit.criterion_id,
                "description": crit.description,
                "beneficiality": crit.min_max,
                "alternativesValuesRaw": crit.alternatives_values_raw,
                "preferenceFunction": crit.preference_function,
                "q-value": crit.q_value,
                "p-value": crit.p_value
            })
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Error fetching criteria: {str(e)}"}), 500


@app.route("/api/delete-criteria-by-id", methods=['POST'])
@jwt_required()
@authorize_request
def delete_criteria_by_id():
    post_data = request.get_json()
    criteria_ids = post_data['criteriaIDs']
    task_id = post_data['taskID']

    try:
        with session_scope() as db:
            criteria = db.query(Criterion).filter_by(task_id=task_id).all()
            for index, crit in enumerate(criteria):
                if crit.criterion_id in criteria_ids:
                    trade_off = db.query(TradeOff).filter_by(task_id=task_id).first()
                    cnt = 0
                    indexes_to_remove = []

                    # determines which pairwise comparisons should be removed.
                    for i in range(len(criteria) - 1):
                        for j in range(i + 1, len(criteria)):
                            if i == index or j == index:
                                indexes_to_remove.append(cnt)
                            cnt += 1

                    if trade_off and trade_off.criteria_weights_raw:
                        temp_criteria_weights_raw = [
                            item for i, item in enumerate(trade_off.criteria_weights_raw[:])
                            if i not in indexes_to_remove
                        ]
                        if temp_criteria_weights_raw:
                            trade_off.criteria_weights_raw = temp_criteria_weights_raw
                            pw = Pairwise(temp_criteria_weights_raw)
                            new_criteria_weights = pw.calculate_eigenvector()
                            trade_off.criteria_weights = new_criteria_weights
                        else:
                            trade_off.criteria_weights_raw = []
                            trade_off.criteria_weights = []
                        db.add(trade_off)
                    db.delete(crit)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Criterion not deleted, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/get-criterion-info", methods=['POST'])
@jwt_required()
@authorize_request
def get_criterion_info():
    post_data = request.get_json()
    criterion_id = post_data['criterionID']

    try:
        with session_scope() as db:
            criterion = db.query(Criterion).filter_by(criterion_id=criterion_id).first()
            if criterion:
                result = {
                    "name": criterion.criterion_name,
                    "description": criterion.description,
                    "beneficiality": criterion.min_max,
                    "alternatives_values": [float(value) for value in criterion.alternatives_values],
                    "criterion_type": criterion.criterion_type,
                    "alternatives_values_raw": [float(value) for value in criterion.alternatives_values_raw]
                }
                status_code = 200
            else:
                result = {"result": "Catastrophic failure!"}
                status_code = 400
            return jsonify(result), status_code
    except Exception as e:
        return jsonify({"error": f"Error retrieving criterion info: {str(e)}"}), 500


@app.route("/api/save-preference-functions", methods=["POST"])
@jwt_required()
@authorize_request
def save_preference_functions():
    post_data = request.get_json()
    preference_functions = post_data["preferenceFunctions"]
    task_id = post_data["taskID"]

    try:
        with session_scope() as db:
            criteria = db.query(Criterion).filter_by(task_id=task_id).order_by(Criterion.criterion_id).all()
            if criteria:
                for index, crit in enumerate(criteria):
                    if index < len(preference_functions):
                        crit.preference_function = preference_functions[index]
                        db.add(crit)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Preference functions not saved, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/save-threshold", methods=["POST"])
@jwt_required()
@authorize_request
def save_threshold():
    post_data = request.get_json()
    threshold = post_data["threshold"]
    threshold_name = post_data["thresholdName"]
    task_id = post_data["taskID"]
    crit_name = post_data["critName"]

    try:
        with session_scope() as db:
            criterion = db.query(Criterion).filter_by(task_id=task_id, criterion_name=crit_name).first()
            if criterion:
                if threshold_name == "q-value":
                    criterion.q_value = threshold
                elif threshold_name == "p-value":
                    criterion.p_value = threshold
                db.add(criterion)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Threshold not saved, error: " + str(e) + "!"}
    return jsonify(response)
