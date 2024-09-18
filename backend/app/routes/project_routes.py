from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, User, Project
from backend.app import app

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)


@app.route("/save-project-to-db", methods=['POST'])
@jwt_required()
def save_project_to_db():
    post_data = request.get_json()
    project_name = post_data['name']
    user_id = get_jwt_identity()
    new_project = Project(project_name=project_name, visibility=False, owner=user_id)
    user = User.query.filter(User.user_id == user_id).first()

    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Project saved!", "projectID": new_project.project_id}

        if flask_session.get("projects") is None:
            flask_session["projects"] = []

        owner = user.first_name + " " + user.last_name
        visibility = "public" if (new_project.visibility == True) else "private"
        flask_session["projects"].append(
            {
                "projectID": new_project.project_id,
                "projectName": project_name,
                "owner": owner,
                "visibility": visibility
            }
        )
        flask_session.modified = True

    return jsonify(response)


@app.route("/get-project-name-by-id/<project_id>", methods=['GET'])
@jwt_required()
def get_project(project_id):
    project_name = ""
    projects = flask_session.get("projects")
    if projects:
        for project in projects:
            if project["projectID"] == project_id:
                project_name = project["project_name"]
                break
    else:
        project = Project.query.filter(Project.project_id == project_id).first()
        project_name = project.project_name

    return jsonify(project_name)


@app.route("/get-projects-by-user-id", methods=['GET'])
@jwt_required()
def get_projects_by_user_id():
    session_projects = flask_session.get("projects")
    if session_projects:
        return jsonify(session_projects)

    user_id = get_jwt_identity()

    projects = (
        sql_session
        .query(Project.project_id, Project.project_name, Project.owner, Project.visibility,
               User.first_name, User.last_name)
        .filter(User.user_id == user_id)
        .filter(Project.owner == user_id).all()
    )

    result = []
    for p in projects:
        owner = p.first_name + " " + p.last_name
        visibility = "public" if (p.visibility == True) else "private"

        result.append(
            {"projectID": p.project_id, "projectName": p.project_name, "visibility": visibility,
             "owner": owner})

    return jsonify(result)


@app.route("/delete-project-by-id", methods=['POST'])
@jwt_required()
def delete_project():
    post_data = request.get_json()
    project_id = post_data['projectID']
    project = Project.query.filter(Project.project_id == project_id).first()
    sql_session.delete(project)

    result = {}
    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not deleted, error: " + str(e) + "!"}
    else:
        projects = flask_session.get("projects")
        if projects:
            for project in projects:
                if project["projectID"] == project_id:
                    flask_session["projects"].remove(project)
                    flask_session.modified = True
                    break

        response = {"result": "success"}

    return jsonify(response)


@app.route("/test-api", methods=['GET', 'POST'])
@jwt_required()
def test_api():
    print(get_jwt_identity())
    print(flask_session.get("tasks"))
    return jsonify({"testkey": "testvalue"})
