from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, Task
from backend.app import app

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from backend.app.routes.utils import save_task_in_session, delete_task_from_session

jwt = JWTManager(app)


@app.route("/api/save-task-to-db", methods=['POST'])
@jwt_required()
def save_task_to_db():
    post_data = request.get_json()
    task_name = post_data['name']
    project_id = post_data['projectID']

    new_task = Task(task_name=task_name, project_id=project_id)
    sql_session.add(new_task)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Criteria not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)


@app.route("/api/get-tasks-by-project-id", methods=['POST'])
@jwt_required()
def get_tasks_by_project_id():
    post_data = request.get_json()
    project_id = post_data['projectID']
    result = []

    tasks = (
        sql_session
        .query(Task.task_id, Task.task_name, Task.created_at)
        .filter(Task.project_id == project_id)
        .all()
    )

    for task in tasks:
        result.append(
            {"taskID": task.task_id, "taskName": task.task_name, "projectID": project_id, "createdAt": task.created_at})

    return jsonify(result)


@app.route("/api/delete-task-by-id", methods=['POST'])
@jwt_required()
def delete_task_by_id():
    post_data = request.get_json()
    task_id = post_data['taskID']
    project_id = post_data['projectID']
    task = Task.query.filter(Task.task_id == task_id).first()
    sql_session.delete(task)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Task not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)
