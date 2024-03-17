from flask import render_template
from backend.app import app

@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")