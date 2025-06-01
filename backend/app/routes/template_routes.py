from flask import jsonify
from werkzeug.exceptions import InternalServerError

from backend.app.db.models import session_scope, Project, Task, Alternative, Criterion, TradeOff
from backend.app import app
from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager

jwt = JWTManager(app)


@app.route("/api/template/dream-home", methods=["GET"])
@jwt_required()
def dream_home():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="Dream Home", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Location", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Home heating system", project_id=new_project.project_id)
            new_task_3 = Task(task_name="Interior Decorations", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2, new_task_3])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            new_trade_off_3 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_3.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2, new_trade_off_3])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/new-car", methods=["GET"])
@jwt_required()
def new_car():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="New Car", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Choose a Car", project_id=new_project.project_id)
            db.add(new_task_1)
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            db.add(new_trade_off_1)
            db.flush()

            new_alt_1 = Alternative(alternative_name="Tesla Model 3", task_id=new_task_1.task_id)
            new_alt_2 = Alternative(alternative_name="Toyota Camry", task_id=new_task_1.task_id)
            new_alt_3 = Alternative(alternative_name="BMW 3 Series", task_id=new_task_1.task_id)
            db.add_all([new_alt_1, new_alt_2, new_alt_3])
            db.flush()

            new_crit_1 = Criterion(
                criterion_name="Price",
                criterion_type="quantitative",
                min_max="min",
                alternatives_values=[39999, 24999, 41999],
                alternatives_values_raw=[39999, 24999, 41999],
                description="Total cost of the car in USD",
                task_id=new_task_1.task_id,
            )
            new_crit_2 = Criterion(
                criterion_name="Fuel Efficiency",
                criterion_type="quantitative",
                min_max="max",
                alternatives_values=[130, 28, 30],
                alternatives_values_raw=[130, 28, 30],
                description="Miles per gallon (MPG) or equivalent",
                task_id=new_task_1.task_id,
            )
            new_crit_3 = Criterion(
                criterion_name="Safety Rating",
                criterion_type="qualitative",
                min_max="max",
                alternatives_values=[5, 5, 4],
                alternatives_values_raw=[5, 5, 4],
                description="Safety rating from crash tests",
                task_id=new_task_1.task_id,
            )
            new_crit_4 = Criterion(
                criterion_name="Maintenance Cost",
                criterion_type="quantitative",
                min_max="min",
                alternatives_values=[500, 1200, 1500],
                alternatives_values_raw=[500, 1200, 1500],
                description="Estimated annual maintenance cost",
                task_id=new_task_1.task_id,
            )
            db.add_all([new_crit_1, new_crit_2, new_crit_3, new_crit_4])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/build-your-pc", methods=["GET"])
@jwt_required()
def build_your_pc():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="Build Your PC", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Processor", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Video Card", project_id=new_project.project_id)
            new_task_3 = Task(task_name="Monitor Configuration", project_id=new_project.project_id)
            new_task_4 = Task(task_name="Laptop vs Desktop", project_id=new_project.project_id)
            new_task_5 = Task(task_name="Prebuilt PCs", project_id=new_project.project_id)
            new_task_6 = Task(task_name="Laptops", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2, new_task_3, new_task_4, new_task_5, new_task_6])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            new_trade_off_3 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_3.task_id)
            new_trade_off_4 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_4.task_id)
            new_trade_off_5 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_5.task_id)
            new_trade_off_6 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_6.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2, new_trade_off_3,
                        new_trade_off_4, new_trade_off_5, new_trade_off_6])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/shopping-list", methods=["GET"])
@jwt_required()
def shopping_list():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="Shopping List", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Choose Pet Food", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Best Coffee", project_id=new_project.project_id)
            new_task_3 = Task(task_name="What's for dinner?", project_id=new_project.project_id)
            new_task_4 = Task(task_name="Clothes", project_id=new_project.project_id)
            new_task_5 = Task(task_name="Home Appliances", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2, new_task_3, new_task_4, new_task_5])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            new_trade_off_3 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_3.task_id)
            new_trade_off_4 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_4.task_id)
            new_trade_off_5 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_5.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2, new_trade_off_3, new_trade_off_4, new_trade_off_5])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/holiday-planner", methods=["GET"])
@jwt_required()
def holiday_planner():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="Holiday Planner", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Choose Location", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Travel Agency", project_id=new_project.project_id)
            new_task_3 = Task(task_name="Choose accommodation", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2, new_task_3])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            new_trade_off_3 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_3.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2, new_trade_off_3])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/new-phone", methods=["GET"])
@jwt_required()
def new_phone():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="New Phone", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Android or Apple", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Choose a phone", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)


@app.route("/api/template/new-guitar", methods=["GET"])
@jwt_required()
def new_guitar():
    user_id = get_jwt_identity()
    try:
        with session_scope() as db:
            new_project = Project(project_name="New Guitar", visibility=False, owner=user_id)
            db.add(new_project)
            db.flush()

            new_task_1 = Task(task_name="Electric or Acoustic", project_id=new_project.project_id)
            new_task_2 = Task(task_name="Choose Pickups", project_id=new_project.project_id)
            new_task_3 = Task(task_name="Choose a Luthier", project_id=new_project.project_id)
            new_task_4 = Task(task_name="Choose a Model", project_id=new_project.project_id)
            db.add_all([new_task_1, new_task_2, new_task_3, new_task_4])
            db.flush()

            new_trade_off_1 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_1.task_id)
            new_trade_off_2 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_2.task_id)
            new_trade_off_3 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_3.task_id)
            new_trade_off_4 = TradeOff(decision_method="topsis", normalization_method="linear",
                                       task_id=new_task_4.task_id)
            db.add_all([new_trade_off_1, new_trade_off_2, new_trade_off_3, new_trade_off_4])
        return jsonify({"projectID": new_project.project_id}), 200
    except Exception as e:
        raise InternalServerError(e)
