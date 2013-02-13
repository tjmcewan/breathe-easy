import pdb
import os
from flask import send_from_directory, jsonify, request
from respirator import app


@app.route('/')
def index():
    return 'Welcome to Respirator!  Take a deep breath and relax.'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/workspaces')
def workspaces():
    return jsonify(success = True)

@app.route('/spaces')
def spaces():
    spaces = app.mask.subscriptions_for_user('tim@mcewan.it')
    space_info = {}
    for space in spaces:
        space_name = space.get_space_name()
        space_info[space_name] = {}
        space_info[space_name]['owner'] = space.get_display_name()
        space_info[space_name]['manage_permission?'] = space.can_manage()
        space_info[space_name]['write_permission?'] = space.can_write()

    return jsonify(space_info)

@app.route('/mirror', methods=['GET', 'POST'])
def mirror():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return jsonify(request.json)
