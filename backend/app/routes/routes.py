from flask import render_template, request, jsonify

from backend.app.db.models import session, User, Project, Task

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

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Project not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Project saved!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/get-project-name-by-id/<project_id>", methods=['GET'])
def get_project(project_id):
    project = Project.query.filter(Project.project_id == project_id).first()

    return jsonify(project.project_name)


@app.route("/get-all-projects", methods=['GET'])
def get_all_projects():
    projects = Project.query.all()

    projects = (
        session
        .query(Project.project_id, Project.project_name, Project.owner, Project.visibility,
               User.first_name, User.last_name, User.user_id)
        .join(User, Project.owner == User.user_id).all()
    )
    print(projects)

    result = []
    for p in projects:
        owner = p.first_name + " " + p.last_name
        visibility = "public" if (p.visibility == True) else "private"

        result.append(
            {"projectID": p.project_id, "projectName": p.project_name, "visibility": visibility,
             "owner": owner})

    return jsonify(result)


@app.route("/save-task-to-db", methods=['POST'])
def save_task_to_db():
    print("asd")
    post_data = request.get_json()
    task_name = post_data['name']
    project_id = post_data['projectID']

    new_task = Task(task_name=task_name, project_id=project_id)
    session.add(new_task)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Task not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Task saved!", "taskID": new_task.task_id}

    print(response)
    return jsonify(response)
