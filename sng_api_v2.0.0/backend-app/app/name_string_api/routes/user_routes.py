import json
from flask import request
from name_string_api import app
from name_string_api.service import user_service as user_svc


@app.route('/users', methods=['GET'])
def get_users():
    role = 'admin'
    role = user_svc.get_role(1)
    if not role.lower() == 'admin':
        return "Not Authorized "
    user_list = user_svc.get_users()

    return json.dumps(user_list)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = user_svc.get_user_by_user_id(user_id)

    return json.dumps(user_data)


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json(force=True)
    user_svc.add_user(data)
    return "User added successfully"


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_svc.delete_user(user_id)
    return "User deleted successfully"
