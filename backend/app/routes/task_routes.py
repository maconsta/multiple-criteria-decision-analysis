from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, Task
from backend.app import app

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)


@app.route("/save-task-to-db", methods=['POST'])
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
        if flask_session.get("tasks") is None:
            flask_session["tasks"] = []

        flask_session["tasks"].append(
            {
                "taskID": new_task.task_id,
                "taskName": new_task.task_name,
                "projectID": project_id
            }
        )

        response = {"result": "success"}
    return jsonify(response)


@app.route("/get-tasks-by-project-id", methods=['POST'])
@jwt_required()
def get_tasks_by_project_id():
    post_data = request.get_json()
    project_id = post_data['projectID']

    session_tasks = flask_session.get("tasks")
    if session_tasks:
        print("logss")
        return jsonify(session_tasks)

    tasks = (
        sql_session
        .query(Task.task_id, Task.task_name)
        .filter(Task.project_id == project_id)
        .all()
    )

    result = []
    for task in tasks:
        result.append(
            {"taskID": task.task_id, "taskName": task.task_name})

    return jsonify(result)
