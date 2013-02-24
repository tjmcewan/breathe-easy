# TODO remove pdb
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


@app.route('/workspaces', methods=['POST'])
def workspaces():
    pdb.set_trace()
    workspace = app.mask.create_workspace(request.json)
    return jsonify(workspace)

@app.route('/workspaces/<workspace>', methods=['GET', 'PUT', 'PATCH'])
def workspace(workspace):
    if request.method == 'GET':
        workspace, status_code = app.mask.show_workspace(workspace)
        return jsonify(workspace), status_code
    else:
        workspace = app.mask.update_workspace(workspace, request.json)
        return jsonify(workspace)

@app.route('/workspaces/<workspace>/subscriptions', methods=['GET', 'POST'])
def subscriptions(workspace):
    if request.method == 'GET':
        subscriptions = app.mask.subscriptions(workspace)
        return jsonify(subscriptions)
    else:
        subscription = app.mask.create_subscription(workspace, request.json)
        return jsonify(subscription)

@app.route('/workspaces/<workspace>/subscriptions/<subscription>', methods=['GET', 'DELETE'])
def subscription(workspace, subscription):
    if request.method == 'GET':
        subscription = app.mask.subscription(request.json)
        return jsonify(subscription)
    else:
        result = app.mask.destroy_subscription(request.json)
        return jsonify(result)

