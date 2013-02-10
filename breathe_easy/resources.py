import os
from flask import send_from_directory
from breathe_easy import app


@app.route('/')
def index():
    return 'Welcome to Breathe Easy!  Take a deep breath and relax.'

@app.route('/workspaces')
def workspaces():
    return 'no workspaces yet'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
