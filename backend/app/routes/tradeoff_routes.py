from flask import request, jsonify

from backend.app.db.models import session as sql_session, Task, TradeOff, Alternative, Criterion, trade_off
from backend.app import app

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from backend.app.routes.utils import save_task_in_session, delete_task_from_session
from backend.mcda.methods.electre import Electre
from backend.mcda.methods.promethee import Promethee
from backend.mcda.methods.topsis import Topsis
from backend.mcda.methods.weightedSum import WeightedSum

jwt = JWTManager(app)

from backend.mcda.core.core import Criterion as Crit, Alternative as Alt, DecisionMatrix, Pairwise


@app.route("/api/save-trade-off-to-db", methods=['POST'])
@jwt_required()
def save_trade_off_to_db():
    post_data = request.get_json()
    criteria_weights = post_data['weights']
    decision_method = post_data['decisionMethod']
    normalization_method = post_data['normalizationMethod']
    task_id = post_data['taskID']
    pairwise = post_data['pairwise']

    if pairwise:
        pw = Pairwise(criteria_weights)
        criteria_weights = pw.calculate_eigenvector()

    new_trade_off = TradeOff(criteria_weights=criteria_weights, decision_method=decision_method,
                             normalization_method=normalization_method, task_id=task_id)
    sql_session.add(new_trade_off)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Trade-Off not saved, error: " + str(e) + "!"}
    else:
        # save_task_in_session(task_id=new_task.task_id, task_name=new_task.task_name, project_id=project_id)

        response = {"result": "success"}

    return jsonify(response)


@app.route("/api/get-trade-off-by-task-id", methods=["POST"])
@jwt_required()
def get_trade_off_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    trade_off = (
        sql_session
        .query(TradeOff.task_id, TradeOff.criteria_weights, TradeOff.decision_method, TradeOff.normalization_method)
        .filter(TradeOff.task_id == task_id)
        .first()
    )

    if not trade_off:
        result = {"success": False, "error": "Resource Not Found."}, 404
    else:
        result = {"success": True, "decisionMethod": trade_off.decision_method,
                  "normalizationMethod": trade_off.normalization_method, "weigths": trade_off.criteria_weights}

    return jsonify(result)


@app.route("/api/delete-trade-off-by-task-id", methods=["POST"])
@jwt_required()
def delete_trade_off_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    trade_off = TradeOff.query.filter(TradeOff.task_id == task_id).first()
    sql_session.delete(trade_off)

    response = {}
    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Trade-Off not deleted, error: " + str(e) + "!"}
    else:
        response = {"success": True}

    return jsonify(response)


@app.route("/api/calculate-result", methods=["POST"])
@jwt_required()
def calculate_result():
    post_data = request.get_json()
    task_id = post_data['taskID']
    project_id = post_data['projectID']

    alternatives_raw = (
        sql_session
        .query(Alternative.task_id, Alternative.alternative_name, Alternative.alternative_id, Alternative.description,
               )
        .filter(Alternative.task_id == task_id)
        .all()
    )

    criteria_raw = (
        sql_session
        .query(Criterion.task_id, Criterion.criterion_name, Criterion.criterion_id,
               Criterion.min_max, Criterion.alternatives_values)
        .filter(Criterion.task_id == task_id)
        .all()
    )

    trade_off_raw = (
        sql_session
        .query(TradeOff.task_id, TradeOff.criteria_weights, TradeOff.decision_method, TradeOff.normalization_method)
        .filter(TradeOff.task_id == task_id)
        .first()
    )

    criteria = []
    values = {}
    for criterion in criteria_raw:
        criteria.append(Crit(name=criterion.criterion_name, min_max=criterion.min_max))

        for (index, val) in enumerate(criterion.alternatives_values):
            if index in values:
                values[index].append(val)
            else:
                values[index] = [val]

    alternatives = []
    for (index, alt) in enumerate(alternatives_raw):
        alternatives.append(Alt(name=alt.alternative_name, values=values[index]))

    normalization_method = trade_off_raw.normalization_method
    if normalization_method == "linear":
        decision_matrix = DecisionMatrix(criteria=criteria, alternatives=alternatives,
                                         normalization_method=DecisionMatrix.normalize)
    elif normalization_method == "l1":
        decision_matrix = DecisionMatrix(criteria=criteria, alternatives=alternatives,
                                         normalization_method=DecisionMatrix.normalize_l1)
    elif normalization_method == "l2":
        decision_matrix = DecisionMatrix(criteria=criteria, alternatives=alternatives,
                                         normalization_method=DecisionMatrix.normalize_l2)

    decision_method = trade_off_raw.decision_method
    result = {"success": True}
    if decision_method == 'topsis':
        topsis = Topsis(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
        result.update({"ranking": topsis.calculate_topsis()})
    elif decision_method == 'ahp':
        pass
    elif decision_method == 'electre':
        electre = Electre(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
        result.update({"ranking":electre.calculate_electre()})
    elif decision_method == 'wsm':
        wsm = WeightedSum(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
        result = wsm.calculate_weighted_sum()
    elif decision_method == 'prometheeii':
        promethee = Promethee(decision_matrix=decision_matrix, weights=trade_off_raw.criteria_weights)
        result.update({"ranking": promethee.calculate_promethee()})
    else:
        result = {"success": False}

    return jsonify(result)
