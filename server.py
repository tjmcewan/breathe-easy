import pdb
import os
from flask import Flask, send_from_directory, jsonify, request
from respirator import Respirator

app = Flask(__name__)

api_key = os.environ['O2_API_KEY']
oxygen_id = os.environ['O2_OXYGEN_ID']
password = os.environ['O2_PASSWORD']
testing = app.config['TESTING']

app.mask = Respirator(api_key, oxygen_id, password, testing)


@app.route('/')
def index():
    return 'Welcome to Respirator!  Take a deep breath and relax.'


@app.route('/spaces', methods=['POST'])
def spaces():
    try:
        name = request.json['name']
        space = app.mask.create_space(name)
        return jsonify(space), 200
    except KeyError:
        error = {"error": "ensure parameters include a 'name' key"}
        return jsonify(error), 400

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = app.mask.get_users()
        return jsonify(users)
    else:
        try:
            attributes = request.json['user']
            user, status_code = app.mask.create_user(attributes)
            return jsonify(user), status_code
        except KeyError:
            error = {"error": "ensure parameters include a 'user' key"}
            return jsonify(error), 400

@app.route('/spaces/<space>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def space(space):
    if request.method == 'GET':
        space, status_code = app.mask.show_space(space)
        return jsonify(space), status_code
    elif request.method == 'DELETE':
        result = app.mask.delete_space(space)
        return jsonify(result)
    else:
        space = app.mask.update_space(space, request.json)
        return jsonify(space)

@app.route('/spaces/<space>/subscriptions', methods=['GET', 'POST'])
def subscriptions(space):
    if request.method == 'GET':
        subscriptions = app.mask.subscriptions(space)
        return jsonify(subscriptions)
    else:
        subscription = app.mask.create_subscription(space, request.json)
        return jsonify(subscription)

@app.route('/spaces/<space>/subscriptions/<subscription>', \
    methods=['GET', 'DELETE'])
def subscription(space, subscription):
    if request.method == 'GET':
        subscription = app.mask.subscription(request.json)
        return jsonify(subscription)
    else:
        result = app.mask.destroy_subscription(request.json)
        return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 3000))
    app.run('0.0.0.0', port)
