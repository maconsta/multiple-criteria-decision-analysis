from flask import request, jsonify
from backend.app.db.models import session_scope, Task, TradeOff
from backend.app import app
from flask_jwt_extended import jwt_required, JWTManager
from backend.app.routes.utils import authorize_request

jwt = JWTManager(app)


@app.route("/api/save-task-to-db", methods=['POST'])
@jwt_required()
@authorize_request
def save_task_to_db():
    post_data = request.get_json()
    task_name = post_data['name']
    project_id = post_data['projectID']

    new_task = Task(task_name=task_name, project_id=project_id)

    try:
        with session_scope() as db:
            db.add(new_task)
            db.flush()

            new_trade_off = TradeOff(decision_method="topsis", normalization_method="linear", task_id=new_task.task_id)
            db.add(new_trade_off)
    except Exception as e:
        return jsonify({"result": "Task not saved, error: " + str(e) + "!"})
    return jsonify({"result": "success"})


@app.route("/api/get-tasks-by-project-id", methods=['POST'])
@jwt_required()
@authorize_request
def get_tasks_by_project_id():
    post_data = request.get_json()
    project_id = post_data['projectID']

    try:
        with session_scope() as db:
            tasks = (
                db.query(Task.task_id, Task.task_name, Task.created_at)
                  .filter(Task.project_id == project_id)
                  .all()
            )
            result = []
            for task in tasks:
                result.append({
                    "taskID": task.task_id,
                    "taskName": task.task_name,
                    "projectID": project_id,
                    "createdAt": task.created_at
                })
        return jsonify(result)
    except Exception as e:
        return jsonify({"result": "Error fetching tasks, error: " + str(e)}), 500


@app.route("/api/delete-task-by-id", methods=['POST'])
@jwt_required()
@authorize_request
def delete_task_by_id():
    post_data = request.get_json()
    task_id = post_data['taskID']
    project_id = post_data['projectID']

    try:
        with session_scope() as db:
            task = db.query(Task).filter(Task.task_id == task_id).first()
            if task is None:
                return jsonify({"result": "Task not found"}), 404
            db.delete(task)
        return jsonify({"result": "success"})
    except Exception as e:
        return jsonify({"result": "Task not deleted, error: " + str(e) + "!"})
