from flask import render_template, request, jsonify

from backend.app.db.models import session, User, Project

from backend.app import app


@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, world!")


# API ROUTES
@app.route("/save-project-to-db", methods=['POST'])
def save_project_to_db():
    post_data = request.get_json()
    project_name = post_data['name']

    # current user should be taken from the session!
    # for now, it will be hardcoded...

    current_user = User.query.filter(User.first_name == "Martin").first()
    new_project = Project(project_name=project_name, visibility=False, owner=current_user.user_id)

    session.add(new_project)

    response = {"result": "Project saved!", "success": True}
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Project not saved, error: " + str(e) + "!", "success": False}

    return jsonify(response)
