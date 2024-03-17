from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*":{"origins": "*"}}) # allows CORS from all sources

from backend.app.routes import routes