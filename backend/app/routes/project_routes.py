from flask import request, jsonify
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    JWTManager
)
from sqlalchemy import or_, any_
from backend.app import app
from backend.app.routes.utils import authorize_request

from backend.app.db.models import session_scope, User, Project

jwt = JWTManager(app)


@app.route("/api/save-project-to-db", methods=["POST"])
@jwt_required()
def save_project_to_db():
    post_data = request.get_json()
    project_name = post_data["name"]
    user_id = get_jwt_identity()

    try:
        with session_scope() as db:
            new_project = Project(project_name=project_name, visibility=False, owner=user_id)
            db.add(new_project)
        response = {"result": "Project saved!", "projectID": new_project.project_id}
    except Exception as e:
        response = {"result": "Project not saved, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/get-project-name-by-id/<project_id>", methods=["GET"])
@jwt_required()
@authorize_request
def get_project(project_id):
    try:
        with session_scope() as db:
            project = db.query(Project).filter(Project.project_id == project_id).first()
            if not project:
                return jsonify({"error": "Project not found"}), 404
            project_name = project.project_name
    except Exception as e:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project_name)



@app.route("/api/get-projects-by-user-id", methods=["GET"])
@jwt_required()
def get_projects_by_user_id():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            user = db.query(User).filter_by(user_id=user_id).first()
            projects = (
                db.query(
                    Project.project_id,
                    Project.project_name,
                    Project.owner,
                    Project.visibility,
                    User.first_name,
                    User.last_name,
                )
                .join(User, User.user_id == Project.owner)
                .filter(
                    or_(
                        Project.owner == user_id,
                        Project.collaborators.any(user.email)
                    )
                )
                .all()
            )
            result = []
            for p in projects:
                owner_full = p.first_name + " " + p.last_name
                visibility = "public" if p.visibility else "private"
                result.append({
                    "projectID": p.project_id,
                    "projectName": p.project_name,
                    "visibility": visibility,
                    "owner": owner_full,
                })
    except Exception as e:
        return jsonify({"error": "Error {e} when querrying for projects"}), 404

    return jsonify(result)


@app.route("/api/delete-project-by-id", methods=["POST"])
@jwt_required()
@authorize_request
def delete_project():
    post_data = request.get_json()
    project_id = post_data["projectID"]
    try:
        with session_scope() as db:
            project = db.query(Project).filter(Project.project_id == project_id).first()
            if not project:
                return jsonify({"error": "Project not found"}), 404
            db.delete(project)
        response = {"result": "success"}
    except Exception as e:
        response = {"result": "Project not deleted, error: " + str(e) + "!"}
    return jsonify(response)


@app.route("/api/change-project-name", methods=["POST"])
@jwt_required()
@authorize_request
def change_project_name():
    post_data = request.get_json()
    project_id = post_data['projectID']
    new_name = post_data['name']

    try:
        with session_scope() as db:
            project = db.query(Project).filter(Project.project_id == project_id).first()
            if not project:
                return jsonify({"error": "Project not found"}), 404
            project.project_name = new_name
        response = {"success": True}
    except Exception as e:
        response = {"result": "Project name not changed, error: " + str(e) + "!", "success": False}
    return jsonify(response)


@app.route("/api/share-project", methods=["POST"])
@jwt_required()
def share_project():
    data = request.get_json()
    project_id = data.get("project_id")
    email = data.get("email")

    try:
        with session_scope() as db:
            project = db.query(Project).filter(Project.project_id == project_id).first()
            if not project:
                return jsonify({"error": "Project not found"}), 404
            if not project.collaborators:
                project.collaborators = []
            if email not in project.collaborators:
                project.collaborators.append(email)
        return jsonify({"message": "Project shared successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to share project: {str(e)}"}), 500


@app.route("/api/projects", methods=["GET"])
@jwt_required()
def get_projects_for_user():
    user_email = get_jwt_identity()
    try:
        with session_scope() as db:
            user_id = db.query(User.user_id).filter_by(email=user_email).scalar()
            projects = (
                db.query(Project)
                .filter((Project.owner == user_id) | (user_email == any_(Project.collaborators)))
                .all()
            )
            result = []
            for project in projects:
                result.append({
                    "project_id": project.project_id,
                    "project_name": project.project_name,
                    "visibility": project.visibility,
                    "owner": project.owner,
                    "collaborators": project.collaborators,
                })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch projects: {str(e)}"}), 500


@app.route("/api/test-api", methods=["GET", "POST"])
@jwt_required()
def test_api():
    print(get_jwt_identity())
    return jsonify({"testkey": "testvalue"})
