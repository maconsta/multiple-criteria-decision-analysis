from flask import session as flask_session

from backend.app.db.models import User

"""
    This file contains utility functions that manage the session. The session is structured in the following way:
    
    session["projects"] = {
        "<project_id>": {
            "projectName": "<project_name>" (str),
            "projectID": <project_id> (int),
            "owner": "<first_name + " " + last_name>" (str),
            "visibility": "<visibility>" (str),
            "tasks": {
                "<task_id>": {
                    "taskID": <task_id> (int),
                    "taskName: "<task_name>" (str),
                    "projectID": <project_id> (int)
                    
                    add alts, crits and methods here later!
                }
            }  
        }
    } 
"""


def save_project_in_session(project_id: int, project_name: str, user_id: int, visibility: str = "private"):
    if flask_session.get("projects") is None:
        flask_session["projects"] = {}

    user = User.query.filter(User.user_id == user_id).first()
    owner = user.first_name + " " + user.last_name

    flask_session["projects"].update({
        project_id: {
            "projectID": project_id,
            "projectName": project_name,
            "owner": owner,
            "visibility": visibility
        }
    })

    flask_session.modified = True


def delete_project_from_session(project_id: int):
    projects = flask_session.get("projects")
    if projects is None:
        return None

    del projects[str(project_id)]

    flask_session.modified = True


def save_task_in_session(task_id: int, task_name: str, project_id: int):
    projects = flask_session.get("projects")
    if projects is None:
        return None

    project = projects.get(project_id)
    if project is None:
        return None

    if project.get("tasks") is None:
        project["tasks"] = {}

    project["tasks"].update({
        task_id: {
            "taskID": task_id,
            "taskName": task_name,
            "projectID": project_id
        }
    })

    flask_session.modified = True


def delete_task_from_session(task_id: int, project_id: int):
    projects = flask_session.get("projects")
    if projects is None:
        return None

    project = projects.get(project_id)
    if project is None:
        return None

    tasks = project.get("tasks")
    del tasks[str(task_id)]

    flask_session.modified = True


def save_alt_in_session(project_id: int, task_id: int, alt_id: int, alt_name: str, alt_description: str):
    task = flask_session.get("projects").get(project_id).get("tasks").get(task_id)

    if task.get("alternatives") is None:
        task["alternatives"] = {}

        task["alternatives"].update({
            alt_id: {
                "name": alt_name,
                "alternativeID": alt_id,
                "description": alt_description,
                # "taskID": task_id # TODO should remove later; redundant
            }
        })

    flask_session.modified = True
