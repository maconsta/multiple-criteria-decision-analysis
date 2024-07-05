from flask import render_template, request, jsonify

from backend.app.db.models import session, User, Project, Task, Criterion, Alternative
from backend.mcda.core.core import Criterion as Crit, Alternative as Alt
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

    # TODO query is not OK, fix later! must add a check for the current active user
    projects = (
        session
        .query(Project.project_id, Project.project_name, Project.owner, Project.visibility,
               User.first_name, User.last_name, User.user_id)
        .join(User, Project.owner == User.user_id).all()
    )

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
        response = {"result": "Criteria not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)


@app.route("/get-tasks-by-project-id", methods=['POST'])
def get_tasks_by_project_id():
    post_data = request.get_json()
    project_id = post_data['projectID']

    tasks = (
        session
        .query(Task.task_id, Task.task_name)
        .filter(Task.project_id == project_id)
        .all()
    )

    result = []
    for task in tasks:
        result.append(
            {"taskID": task.task_id, "taskName": task.task_name})

    return jsonify(result)


@app.route("/save-criterion-to-db", methods=['POST'])
def save_criterion_to_db():
    post_data = request.get_json()
    criterion_name = post_data['name']
    criterion_beneficiality = post_data['beneficiality']
    criterion_description = post_data['description']
    task_id = post_data['taskID']

    new_criterion = Criterion(criterion_name=criterion_name, min_max=criterion_beneficiality,
                              description=criterion_description, task_id=task_id)
    session.add(new_criterion)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Criterion not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Criterion Saved!", "criterion_id": new_criterion.criterion_id}

    return jsonify(response)


@app.route("/get-criteria-by-task-id", methods=['POST'])
def get_criteria_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    criteria = (
        session
        .query(Criterion.task_id, Criterion.criterion_name, Criterion.criterion_id, Criterion.description,
               Criterion.min_max)
        .filter(Criterion.task_id == task_id)
        .all()
    )

    result = []
    for crit in criteria:
        result.append(
            {"taskID": crit.task_id, "name": crit.criterion_name, "criterionID": crit.criterion_id,
             "description": crit.description, "beneficiality": crit.min_max})

    return jsonify(result)


@app.route("/delete-criteria-by-id", methods=['POST'])
def delete_criteria_by_id():
    post_data = request.get_json()
    criteria_ids = post_data['criteriaIDs']

    for crit_id in criteria_ids:
        criterion = Criterion.query.get(crit_id)

        if criterion:
            session.delete(criterion)

    response = {}
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Criterion not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)


@app.route("/save-alternative-to-db", methods=['POST'])
def save_alternative_to_db():
    post_data = request.get_json()
    alternative_name = post_data['name']
    alternative_description = post_data['description']
    task_id = post_data['taskID']

    new_alternative = Alternative(alternative_name=alternative_name,
                                  description=alternative_description, task_id=task_id)
    session.add(new_alternative)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Alternative not saved, error: " + str(e) + "!"}
    else:
        response = {"result": "Alternative Saved!", "alternative_id": new_alternative.alternative_id}

    return jsonify(response)


@app.route("/get-alternatives-by-task-id", methods=['POST'])
def get_alternatives_by_task_id():
    post_data = request.get_json()
    task_id = post_data['taskID']

    alternatives = (
        session
        .query(Alternative.task_id, Alternative.alternative_name, Alternative.alternative_id, Alternative.description,
               )
        .filter(Alternative.task_id == task_id)
        .all()
    )

    result = []
    for alt in alternatives:
        result.append(
            {"taskID": alt.task_id, "name": alt.alternative_name, "alternativeID": alt.alternative_id,
             "description": alt.description})

    return jsonify(result)


@app.route("/delete-alternatives-by-id", methods=['POST'])
def delete_alternatives_by_id():
    post_data = request.get_json()
    alternatives_ids = post_data['alternativesIDs']

    for alt_id in alternatives_ids:
        alt = Alternative.query.get(alt_id)

        if alt:
            session.delete(alt)

    response = {}
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        response = {"result": "Alternatives not deleted, error: " + str(e) + "!"}
    else:
        response = {"result": "success"}

    return jsonify(response)


@app.route("/calculate-results", methods=['POST'])
def calculate_results():
    post_data = request.get_json()
    weight_matrix_raw = post_data['weightMatrix']
    alternatives_raw = post_data['alternatives']
    criteria_raw = post_data['criteria']

    # print(weight_matrix_raw)
    # print(alternatives_raw)
    # print(criteria_raw)

    criteria = []
    for crit in criteria_raw:
        c = Crit(name=crit['name'], min_max=crit['beneficiality'])
        criteria.append(c)

    alternatives = []
    # for alt in alternatives_raw:
        # alternatives need values, fix that first and come back
        # a = Alt()

    print(criteria)

    return jsonify("test")
