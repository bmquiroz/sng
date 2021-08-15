import json
from flask import request
from name_string_api import app
from name_string_api.service import user_service as user_svc
from werkzeug.security import generate_password_hash, check_password_hash
from name_string_api.models.users import ApiUser
import name_string_api.database_utility as db_util
import uuid 


# @app.route('/create_api_user', methods=['POST'])
# def add_api_user():
#     data = request.get_json(force=True)
#     user_svc.add_api_user(data)
#     return "API user added successfully"


@app.route('/create_api_user', methods=['GET', 'POST'])
def add_api_user():
    data = request.get_json(force=True)
    hashed_password = generate_password_hash(data['password'], method='sha256')
 
    user = ApiUser(public_id=str(uuid.uuid4()), username=data['username'], password=hashed_password)
    db_util.db.session.add(user)
    db_util.db.session.commit()
    db_util.db.session.close()

    # user_svc.add_api_user(data)
    return "API user added successfully"


@app.route('/users', methods=['GET'])
def get_users():
    role = 'admin'
    role = user_svc.get_role(1)
    if not role.lower() == 'admin':
        return "Not authorized"
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
