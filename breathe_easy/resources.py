import os
from flask import send_from_directory, jsonify
from breathe_easy import app


@app.route('/')
def index():
    return 'Welcome to Breathe Easy!  Take a deep breath and relax.'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/workspaces')
def workspaces():
    return jsonify(success = True)
