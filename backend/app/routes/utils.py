from functools import wraps

from flask import request
from werkzeug.exceptions import Forbidden

from backend.app.db.models import session as sql_session, Project, User

from flask_jwt_extended import get_jwt_identity


def authorize_request(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = int(get_jwt_identity())
        if request.method == "POST":
            post_data = request.get_json()
            project_id = post_data.get("projectID")
        elif request.method == "GET":
            project_id = kwargs.get("project_id")

        current_user = User.query.filter_by(user_id=user_id).first()

        project = (
            sql_session
            .query(Project)
            .filter(Project.project_id == project_id)
            .first()
        )

        if not project or (project.owner != user_id and current_user.email not in project.collaborators):
            raise Forbidden()

        return f(*args, **kwargs)
    return decorated
