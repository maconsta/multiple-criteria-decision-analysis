from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, Task
from backend.app import app

from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from backend.app.routes.utils import save_task_in_session, delete_task_from_session

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
        save_task_in_session(task_id=new_task.task_id, task_name=new_task.task_name, project_id=project_id)

        response = {"result": "success"}
    return jsonify(response)


@app.route("/get-tasks-by-project-id", methods=['POST'])
@jwt_required()
def get_tasks_by_project_id():
    post_data = request.get_json()
    project_id = post_data['projectID']
    result = []

    projects = flask_session.get("projects")
    if projects:
        project = projects.get(project_id)
        if project:
            tasks = project.get("tasks")
            if tasks:
                return jsonify([task for task in tasks.values()])

    tasks = (
        sql_session
        .query(Task.task_id, Task.task_name)
        .filter(Task.project_id == project_id)
        .all()
    )

    for task in tasks:
        save_task_in_session(task_id=task.task_id, task_name=task.task_name, project_id=project_id)

        result.append(
            {"taskID": task.task_id, "taskName": task.task_name, "projectID": project_id})

    return jsonify(result)


@app.route("/delete-task-by-id", methods=['POST'])
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
        response = {"result": "Project not deleted, error: " + str(e) + "!"}
    else:
        delete_task_from_session(task_id=task_id, project_id=project_id)
        response = {"result": "success"}

    return jsonify(response)
