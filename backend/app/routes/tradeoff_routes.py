from flask import request, jsonify
from werkzeug.exceptions import InternalServerError

from backend.app.db.models import session_scope, Task, TradeOff, Alternative, Criterion
from backend.app import app

from flask_jwt_extended import jwt_required, JWTManager
jwt = JWTManager(app)

from backend.app.routes.utils import authorize_request
from backend.mcda.methods.ahp import AHP
from backend.mcda.methods.electre import Electre
from backend.mcda.methods.promethee import Promethee
from backend.mcda.methods.topsis import Topsis
from backend.mcda.methods.weightedSum import WeightedSum

from backend.mcda.core.core import (
    Criterion as Crit,
    Alternative as Alt,
    DecisionMatrix,
    Pairwise,
)


@app.route("/api/save-trade-off-to-db", methods=["POST"])
@jwt_required()
@authorize_request
def save_trade_off_to_db():
    post_data = request.get_json()
    criteria_weights = post_data["weights"]
    task_id = post_data["taskID"]

    criteria_weights = [float(value) for value in criteria_weights]
    criteria_weights_raw = criteria_weights

    pw = Pairwise(criteria_weights)
    criteria_weights_clean = pw.calculate_eigenvector()

    try:
        with session_scope() as db:
            trade_off_record = db.query(TradeOff).filter_by(task_id=task_id).first()
            # if trade_off_record is None: #todo check if this is needed
            #     trade_off_record = TradeOff(task_id=task_id)
            trade_off_record.criteria_weights = criteria_weights_clean
            trade_off_record.criteria_weights_raw = criteria_weights_raw
            db.add(trade_off_record)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Trade-Off not saved, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/get-trade-off-by-task-id", methods=["POST"])
@jwt_required()
@authorize_request
def get_trade_off_by_task_id():
    post_data = request.get_json()
    task_id = post_data["taskID"]

    try:
        with session_scope() as db:
            trade_off_record = (
                db.query(
                    TradeOff.task_id,
                    TradeOff.criteria_weights,
                    TradeOff.decision_method,
                    TradeOff.normalization_method,
                    TradeOff.criteria_weights_raw,
                )
                .filter(TradeOff.task_id == task_id)
                .first()
            )
        if not trade_off_record:
            return jsonify({"success": False, "error": "Resource Not Found."}), 404
        else:
            result = {
                "success": True,
                "decisionMethod": trade_off_record.decision_method,
                "normalizationMethod": trade_off_record.normalization_method,
                "weights": trade_off_record.criteria_weights,
                "criteriaWeightsRaw": trade_off_record.criteria_weights_raw,
            }
            return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/delete-trade-off-by-task-id", methods=["POST"])
@jwt_required()
def delete_trade_off_by_task_id():
    post_data = request.get_json()
    task_id = post_data["taskID"]
    try:
        with session_scope() as db:
            trade_off_record = db.query(TradeOff).filter(TradeOff.task_id == task_id).first()
            if trade_off_record:
                db.delete(trade_off_record)
        response = {"success": True}
    except Exception as e:
        response = {"result": "Trade-Off not deleted, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/calculate-result", methods=["POST"])
@jwt_required()
@authorize_request
def calculate_result():
    post_data = request.get_json()
    task_id = post_data["taskID"]
    project_id = post_data["projectID"]

    try:
        with session_scope() as db:
            alternatives_raw = (
                db.query(
                    Alternative.task_id,
                    Alternative.alternative_name,
                    Alternative.alternative_id,
                    Alternative.description,
                )
                .filter(Alternative.task_id == task_id)
                .all()
            )
            criteria_raw = (
                db.query(
                    Criterion.task_id,
                    Criterion.criterion_name,
                    Criterion.criterion_id,
                    Criterion.min_max,
                    Criterion.alternatives_values,
                    Criterion.preference_function,
                    Criterion.q_value,
                    Criterion.p_value,
                )
                .filter(Criterion.task_id == task_id)
                .all()
            )
            trade_off_raw = (
                db.query(
                    TradeOff.task_id,
                    TradeOff.criteria_weights,
                    TradeOff.decision_method,
                    TradeOff.normalization_method,
                )
                .filter(TradeOff.task_id == task_id)
                .first()
            )

        if not trade_off_raw or not trade_off_raw.criteria_weights:
            raise ValueError("Add trade-offs!")

        criteria = []
        values = {}
        preference_function = []
        q_values, p_values = [], []
        for criterion in criteria_raw:
            criteria.append(Crit(name=criterion.criterion_name, min_max=criterion.min_max))
            preference_function.append(criterion.preference_function)
            p_values.append(float(criterion.p_value) if criterion.p_value else 1)
            q_values.append(float(criterion.q_value) if criterion.q_value else 0)
            for index, val in enumerate(criterion.alternatives_values):
                values.setdefault(index, []).append(val)

        alternatives = []
        for index, alt in enumerate(alternatives_raw):
            alternatives.append(Alt(name=alt.alternative_name, values=values[index]))

        normalization_method = trade_off_raw.normalization_method
        if normalization_method == "linear":
            decision_matrix = DecisionMatrix(
                criteria=criteria,
                alternatives=alternatives,
                normalization_method=DecisionMatrix.normalize,
            )
        elif normalization_method == "l1":
            decision_matrix = DecisionMatrix(
                criteria=criteria,
                alternatives=alternatives,
                normalization_method=DecisionMatrix.normalize_l1,
            )
        elif normalization_method == "l2":
            decision_matrix = DecisionMatrix(
                criteria=criteria,
                alternatives=alternatives,
                normalization_method=DecisionMatrix.normalize_l2,
            )
        else:
            decision_matrix = DecisionMatrix(
                criteria=criteria,
                alternatives=alternatives,
                normalization_method=DecisionMatrix.normalize,
            )

        decision_matrix_data = {
            "criteria": [crit.name for crit in criteria],
            "alternatives": [alt.name for alt in alternatives],
            "values": [alt.values for alt in alternatives],
        }

        decision_method = trade_off_raw.decision_method
        result = {"success": True}
        if decision_method == "topsis":
            topsis = Topsis(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
            result.update({"ranking": topsis.calculate_topsis()})
        elif decision_method == "ahp":
            ahp = AHP(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
            result.update({"ranking": ahp.calculate_ahp()})
        elif decision_method == "electre":
            electre = Electre(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
            result.update({"ranking": electre.calculate_electre()})
        elif decision_method == "wsm":
            wsm = WeightedSum(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
            result.update({"ranking": wsm.calculate_weighted_sum()})
        elif decision_method == "prometheeii":
            promethee = Promethee(
                decision_matrix=decision_matrix,
                weights=trade_off_raw.criteria_weights,
                preference_type=preference_function,
                q_values=q_values,
                p_values=p_values,
            )
            result.update({"ranking": promethee.calculate_promethee()})
        else:
            result = {"success": False}

        result.update({"decision_matrix": decision_matrix_data})
        return jsonify(result)
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/save-method-to-db", methods=["POST"])
@jwt_required()
@authorize_request
def save_method_to_db():
    post_data = request.get_json()
    decision_method = post_data["decisionMethod"]
    normalization_method = post_data["normalizationMethod"]
    task_id = post_data["taskID"]
    try:
        with session_scope() as db:
            trade_off_record = db.query(TradeOff).filter_by(task_id=task_id).first()
            if trade_off_record is None:
                trade_off_record = TradeOff(task_id=task_id)
            trade_off_record.decision_method = decision_method
            trade_off_record.normalization_method = normalization_method
            db.add(trade_off_record)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Method not saved, error: " + str(e) + "!"}
    return jsonify(response)
