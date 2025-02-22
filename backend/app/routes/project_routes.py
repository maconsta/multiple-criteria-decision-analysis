from flask import request, jsonify, session as flask_session

from backend.app.db.models import session as sql_session, User, Project
from backend.app import app

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from sqlalchemy import or_, any_

jwt = JWTManager(app)


@app.route("/api/save-project-to-db", methods=["POST"])
@jwt_required()
def save_project_to_db():
    post_data = request.get_json()
    project_name = post_data["name"]
    user_id = get_jwt_identity()
    new_project = Project(project_name=project_name, visibility=False, owner=user_id)

    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Project saved!", "projectID": new_project.project_id}

        # save_project_in_session(project_id=new_project.project_id, project_name=project_name, user_id=user_id)

    return jsonify(response)


@app.route("/api/get-project-name-by-id/<project_id>", methods=["GET"])
@jwt_required()
def get_project(project_id):
    project_name = ""
    # projects = flask_session.get("projects")
    # if projects:
    #     project = projects.get(project_id)
    #
    #     if project:
    #         project_name = project.get("projectName")
    # else:

    project = Project.query.filter(Project.project_id == project_id).first()
    project_name = project.project_name

    return jsonify(project_name)


@app.route("/api/get-projects-by-user-id", methods=["GET"])
@jwt_required()
def get_projects_by_user_id():

    # projects = flask_session.get("projects")
    # if projects:
    #     result = [value for value in projects.values()]
    #     return jsonify(result)

    user_id = get_jwt_identity()

    user = sql_session.query(User).filter_by(user_id=user_id).first()

    projects = (
        sql_session.query(
            Project.project_id,
            Project.project_name,
            Project.owner,
            Project.visibility,
            User.first_name,
            User.last_name,
        )
        .join(User, User.user_id == Project.owner)
        .filter(or_(Project.owner == user_id, Project.collaborators.any(user.email)))
        .all()
    )

    result = []
    for p in projects:
        owner = p.first_name + " " + p.last_name
        visibility = "public" if (p.visibility == True) else "private"

        result.append(
            {
                "projectID": p.project_id,
                "projectName": p.project_name,
                "visibility": visibility,
                "owner": owner,
            }
        )

        # save_project_in_session(project_id=p.project_id, project_name=p.project_name, user_id=user_id,
        #                        visibility=visibility)

    return jsonify(result)


@app.route("/api/delete-project-by-id", methods=["POST"])
@jwt_required()
def delete_project():
    post_data = request.get_json()
    project_id = post_data["projectID"]
    project = Project.query.filter(Project.project_id == project_id).first()
    sql_session.delete(project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not deleted, error: " + str(e) + "!"}
    else:
        # delete_project_from_session(project_id=project_id)

        response = {"result": "success"}

    return jsonify(response)

@app.route("/api/change-project-name", methods=['POST'])
@jwt_required()
def change_project_name():
    post_data = request.get_json()
    project_id = post_data['projectID']
    new_name = post_data['name']

    project = Project.query.filter(Project.project_id == project_id).first()

    project.project_name = new_name

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project name not changed, error: " + str(e) + "!", "success": False}
    else:
        response = {"success": True}

    return jsonify(response)

@app.route("/api/share-project", methods=["POST"])
@jwt_required()
def share_project():
    data = request.get_json()
    project_id = data.get("project_id")
    email = data.get("email")

    project = (
        sql_session.query(Project).filter(Project.project_id == project_id).first()
    )
    if not project:
        return jsonify({"error": "Project not found"}), 404

    if not project.collaborators:
        project.collaborators = []

    if email not in project.collaborators:
        project.collaborators.append(email)

    try:
        sql_session.commit()
        return jsonify({"message": "Project shared successfully!"}), 200
    except Exception as e:
        sql_session.rollback()
        return jsonify({"error": f"Failed to share project: {str(e)}"}), 500


@app.route("/api/projects", methods=["GET"])
@jwt_required()
def get_projects_for_user():
    user_email = get_jwt_identity()

    try:
        projects = (
            sql_session.query(Project)
            .filter(
                (
                    Project.owner
                    == sql_session.query(User.user_id)
                    .filter_by(email=user_email)
                    .scalar()
                )
                | (user_email == any_(Project.collaborators))
            )
            .all()
        )

        result = [
            {
                "project_id": project.project_id,
                "project_name": project.project_name,
                "visibility": project.visibility,
                "owner": project.owner,
                "collaborators": project.collaborators,
            }
            for project in projects
        ]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Failed to fetch projects: {str(e)}"}), 500


@app.route("/api/test-api", methods=["GET", "POST"])
@jwt_required()
def test_api():
    print(get_jwt_identity())
    return jsonify({"testkey": "testvalue"})