from flask import Flask
from flask_cors import CORS
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = env.get("JWT_SECRET_KEY")
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SAMESITE"] = "None"
app.config["JWT_COOKIE_SECURE"] = "Secure"

CORS(app, origins="http://www.localhost:8080", supports_credentials=True, allow_headers=["x-csrf-token", "content-type"
                                                                                         ])  # allows CORS from localhost only

from backend.app.routes import routes
