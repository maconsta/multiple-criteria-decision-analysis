from flask import Flask
from flask_cors import CORS
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)

# JWT CONFIG
app.config["JWT_SECRET_KEY"] = env.get("JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SAMESITE"] = "None"
app.config["JWT_COOKIE_SECURE"] = "Secure"

# FLASK CONFIG
app.config["SECRET_KEY"] = env.get("JWT_SECRET_KEY")  # same secret key as jwt
app.config["SESSION_COOKIE_SECURE"] = "Secure"
app.config["SESSION_COOKIE_SAMESITE"] = "None"

CORS(
    app,
    origins=["http://localhost:8080", "http://www.localhost:8080"],
    supports_credentials=True,
    allow_headers=["x-csrf-token", "content-type"],
)  # allows CORS from localhost only

from backend.app.routes import project_routes
from backend.app.routes import task_routes
from backend.app.routes import authentication_routes
from backend.app.routes import alternative_routes
from backend.app.routes import user_profile_routes
