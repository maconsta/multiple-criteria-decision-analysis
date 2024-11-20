from flask import request, jsonify

from backend.app.db.models import session as sql_session, Task, TradeOff
from backend.app import app

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from backend.app.routes.utils import save_task_in_session, delete_task_from_session

jwt = JWTManager(app)


@app.route("/save-trade-off-to-db", methods=['POST'])
@jwt_required()
def save_trade_off_to_db():
    post_data = request.get_json()
    criteria_weights = post_data['weights']
    decision_method = post_data['decisionMethod']
    normalization_method = post_data['normalizationMethod']
    task_id = post_data['taskID']

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

    return (jsonify(response))


@app.route("/get-trade-off-by-task-id", methods=["POST"])
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

    result = {"success": True, "decisionMethod": trade_off.decision_method,
              "normalizationMethod": trade_off.normalization_method, "weigths": trade_off.criteria_weights}

    return jsonify(result)
