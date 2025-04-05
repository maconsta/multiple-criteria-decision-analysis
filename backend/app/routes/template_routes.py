from flask import jsonify

from backend.app.db.models import (
    session as sql_session,
    Project,
    Task,
    Alternative,
    Criterion,
)
from backend.app import app

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)


@app.route("/api/template/dream-home", methods=["GET"])
@jwt_required()
def dream_home():
    user_id = get_jwt_identity()

    new_project = Project(project_name="Dream Home", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Location", project_id=new_project.project_id)
    new_task_2 = Task(
        task_name="Home heating system", project_id=new_project.project_id
    )
    new_task_3 = Task(task_name="Window Frames", project_id=new_project.project_id)
    new_task_4 = Task(task_name="Choosing materials", project_id=new_project.project_id)
    new_task_5 = Task(
        task_name="Interior Decorations", project_id=new_project.project_id
    )

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)
    sql_session.add(new_task_4)
    sql_session.add(new_task_5)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/api/template/new-car", methods=["GET"])
@jwt_required()
def new_car():
    user_id = get_jwt_identity()

    new_project = Project(project_name="New Car", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Choose Interior", project_id=new_project.project_id)
    new_task_2 = Task(task_name="Engine Type", project_id=new_project.project_id)
    new_task_3 = Task(task_name="Choose a Car", project_id=new_project.project_id)

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    new_alt_1 = Alternative(
        alternative_name="Tesla Model 3", task_id=new_task_3.task_id
    )
    new_alt_2 = Alternative(alternative_name="Toyota Camry", task_id=new_task_3.task_id)
    new_alt_3 = Alternative(alternative_name="BMW 3 Series", task_id=new_task_3.task_id)

    sql_session.add(new_alt_1)
    sql_session.add(new_alt_2)
    sql_session.add(new_alt_3)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Alternatives not added, error: " + str(e) + "!"}
    else:
        response = {
            "result": "Alternatives added!",
            "projectID": new_project.project_id,
        }

    new_crit_1 = Criterion(
        criterion_name="Price",
        criterion_type="quantitative",
        min_max="min",
        alternatives_values=[39999, 24999, 41999],
        description="Total cost of the car in USD",
        task_id=new_task_3.task_id,
    )

    new_crit_2 = Criterion(
        criterion_name="Fuel Efficiency",
        criterion_type="quantitative",
        min_max="max",
        alternatives_values=[130, 28, 30],
        description="Miles per gallon (MPG) or equivalent",
        task_id=new_task_3.task_id,
    )

    new_crit_3 = Criterion(
        criterion_name="Safety Rating",
        criterion_type="qualitative",
        min_max="max",
        alternatives_values=[5, 5, 4],
        description="Safety rating from crash tests",
        task_id=new_task_3.task_id,
    )

    new_crit_4 = Criterion(
        criterion_name="Maintenance Cost",
        criterion_type="quantitative",
        min_max="min",
        alternatives_values=[500, 1200, 1500],
        description="Estimated annual maintenance cost",
        task_id=new_task_3.task_id,
    )

    sql_session.add(new_crit_1)
    sql_session.add(new_crit_2)
    sql_session.add(new_crit_3)
    sql_session.add(new_crit_4)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Criterion not added, error: " + str(e) + "!"}
    else:
        response = {
            "result": "Criterion added!",
            "projectID": new_project.project_id,
        }

    return jsonify(response)


@app.route("/api/template/build-your-pc", methods=["GET"])
@jwt_required()
def build_your_pc():
    user_id = get_jwt_identity()

    new_project = Project(project_name="Build Your PC", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Processor", project_id=new_project.project_id)
    new_task_2 = Task(task_name="Video Card", project_id=new_project.project_id)
    new_task_3 = Task(
        task_name="Monitor Configuration", project_id=new_project.project_id
    )
    new_task_4 = Task(task_name="Laptop vs Desktop", project_id=new_project.project_id)
    new_task_5 = Task(task_name="Prebuilt PCs", project_id=new_project.project_id)
    new_task_6 = Task(task_name="Laptops", project_id=new_project.project_id)

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)
    sql_session.add(new_task_4)
    sql_session.add(new_task_5)
    sql_session.add(new_task_6)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/api/template/shopping-list", methods=["GET"])
@jwt_required()
def shopping_list():
    user_id = get_jwt_identity()

    new_project = Project(project_name="Shopping List", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Choose Pet Food", project_id=new_project.project_id)
    new_task_2 = Task(task_name="Best Coffee", project_id=new_project.project_id)
    new_task_3 = Task(task_name="What's for dinner?", project_id=new_project.project_id)
    new_task_4 = Task(task_name="Clothes", project_id=new_project.project_id)
    new_task_5 = Task(task_name="Home Appliances", project_id=new_project.project_id)

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)
    sql_session.add(new_task_4)
    sql_session.add(new_task_5)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/api/template/holiday-planner", methods=["GET"])
@jwt_required()
def holiday_planner():
    user_id = get_jwt_identity()

    new_project = Project(
        project_name="Holiday Planner", visibility=False, owner=user_id
    )
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Choose Location", project_id=new_project.project_id)
    new_task_2 = Task(task_name="Travel Agency", project_id=new_project.project_id)
    new_task_3 = Task(
        task_name="Choose accommodation", project_id=new_project.project_id
    )

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/api/template/new-phone", methods=["GET"])
@jwt_required()
def new_phone():
    user_id = get_jwt_identity()

    new_project = Project(project_name="New Phone", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(task_name="Android or Apple", project_id=new_project.project_id)
    new_task_2 = Task(task_name="Choose a phone", project_id=new_project.project_id)

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)


@app.route("/api/template/new-guitar", methods=["GET"])
@jwt_required()
def new_guitar():
    user_id = get_jwt_identity()

    new_project = Project(project_name="New Guitar", visibility=False, owner=user_id)
    sql_session.add(new_project)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Project not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Project created!", "projectID": new_project.project_id}

    new_task_1 = Task(
        task_name="Electric or Acoustic", project_id=new_project.project_id
    )
    new_task_2 = Task(task_name="Choose Pickups", project_id=new_project.project_id)
    new_task_3 = Task(task_name="Choose a Luthier", project_id=new_project.project_id)
    new_task_4 = Task(task_name="Choose a Model", project_id=new_project.project_id)

    sql_session.add(new_task_1)
    sql_session.add(new_task_2)
    sql_session.add(new_task_3)
    sql_session.add(new_task_4)

    try:
        sql_session.commit()
    except Exception as e:
        sql_session.rollback()
        sql_session.flush()
        response = {"result": "Tasks not created, error: " + str(e) + "!"}
    else:
        response = {"result": "Tasks created!", "projectID": new_project.project_id}

    return jsonify(response)
