import os
from flask import send_from_directory, jsonify
from breathe_easy import app


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
    spaces = app.respirator.subscriptions_for_user('tim@mcewan.it')
    space_info = {}
    for space in spaces:
        space_name = space.get_space_name()
        space_info[space_name] = {}
        space_info[space_name]['owner'] = space.get_display_name()
        space_info[space_name]['manage_permission?'] = space.can_manage()
        space_info[space_name]['write_permission?'] = space.can_write()

    return jsonify(space_info)

# @app.route('/mirror')
# def mirror():
#     return jsonify
