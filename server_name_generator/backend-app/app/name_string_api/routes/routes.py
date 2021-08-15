import sys
import json
import os
from name_string_api import app
from name_string_api.models.users import User
from name_string_api.models.users import ApiUser
from name_string_api.service import user_service as user_svc
from flask import render_template, request, redirect, url_for, abort, jsonify, Response, make_response, send_from_directory
from flask_login import LoginManager, UserMixin, login_required, login_user,\
    logout_user, current_user
from flask_ldap3_login.forms import LDAPLoginForm
from flask_ldap3_login import LDAP3LoginManager, AuthenticationResponseStatus
from werkzeug.security import generate_password_hash, check_password_hash
import name_string_api.database_utility as db_util
from flask_cors import CORS, cross_origin
import uuid 
import jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from datetime import datetime, timedelta 
import logging
logging.getLogger('flask_ldap3_login').setLevel(logging.DEBUG)
logging.basicConfig()


ldap_host = os.environ['LDAP_HOST']
ldap_bind_user_password = os.environ['LDAP_BIND_USER_PASSWORD']


app.config['DEBUG'] = True
app.config['LDAP_HOST'] = ldap_host
app.config['LDAP_BASE_DN'] = 'DC=home,DC=redchip,DC=net'
app.config['LDAP_USER_DN'] = 'OU=NJ'
app.config['LDAP_USER_LOGIN_ATTR'] = 'cn'
app.config['LDAP_USER_RDN_ATTR'] = 'CN'
app.config['LDAP_USER_OBJECT_FILTER'] = '(objectclass=person)'
app.config['LDAP_USER_SEARCH_SCOPE'] = 'SUBTREE'
app.config['LDAP_SEARCH_FOR_GROUPS'] = 'True'
app.config['LDAP_GROUP_DN'] = 'CN=SNG_Users,OU=Groups,OU=NJ'
app.config['LDAP_GROUP_OBJECT_FILTER'] = '(objectclass=group)'
app.config['LDAP_GROUP_MEMBERS_ATTR'] = 'member'
app.config['LDAP_GROUP_SEARCH_SCOPE'] = 'SUBTREE'
app.config['LDAP_BIND_USER_DN'] = 'CN=Administrator,CN=Users,DC=home,DC=redchip,DC=net'
app.config['LDAP_BIND_AUTHENTICATION_TYPE'] = 'SIMPLE'
app.config['LDAP_BIND_USER_PASSWORD'] = ldap_bind_user_password


login_manager = LoginManager(app) # Setup a Flask-Login Manager
ldap_manager = LDAP3LoginManager(app)  # Setup a LDAP3 Login Manager
CORS(app)
jwt = JWTManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/<path:path>', methods=['GET', 'POST'])
def static_proxy(path):
  return send_from_directory('./', path)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/api/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        data = request.get_json(force=True)
        username = data.get("username")
        password = data.get("password")

        result = ldap_manager.authenticate(username, password)

        if result.status == AuthenticationResponseStatus.success:
            user_dn_dict = ldap_manager.get_user_info_for_username(username)
            print(user_dn_dict)

            try:
                for key, value in user_dn_dict.items():
                    if key == 'dn':
                        user_dn = value
                        print(user_dn)
            except:
                print("Something went wrong")
                return redirect(url_for('login'))
            else:
                group_membership = ldap_manager.get_user_groups(user_dn)
                print(group_membership)

                if group_membership:

                    user_id = user_svc.validate_user(username)

                    if user_id == None:
                        user = User(
                            username = username,
                            public_id = str(uuid.uuid4()))
                        db_util.db.session.add(user)
                        db_util.db.session.commit()
                        db_util.db.session.close()
                        user_id = user_svc.validate_user(username)
                        user = User(user_id)
                        login_user(user, remember=True)
                        # Generates the JWT token using flask_jwt_extended
                        access_token = create_access_token(identity=username)
                        response = make_response(jsonify({"access_token": access_token}), 200)
                        response.headers.add('Access-Control-Allow-Origin', 'http://sng.home.redchip.net')
                        return response
                        
                        # Print JWT token
                        # return make_response(jsonify({'token' : access_token}), 201)

                    else:
                        user_id = user_svc.validate_user(username)
                        user = User(user_id)
                        login_user(user, remember=True)
                        response = jsonify({"response":'Login successful'})
                        response.headers.add('Access-Control-Allow-Origin', 'http://sng.home.redchip.net')
                        return response
                else:
                    return jsonify({"response":'Login not successful'})
        else:
            return jsonify({"response":'Login not successful'})
    return render_template('login.html')
    

# @app.route('/api/api_auth', methods=['GET', 'POST'])
# def login_api_user():

#    auth = request.authorization 

#    if not auth or not auth.username or not auth.password:  
#       return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "Login required"'})
#    else:
#        username = request.form['username']
#        password = request.form['password']
#        user_id = user_svc.validate_api_user(username, password)
     
#    if check_password_hash(user_id.password, auth.password):  
#       token = jwt.encode({'public_id': user_id.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])  
#       return jsonify({'token' : token.decode('UTF-8')}) 

#    return make_response('Could not verify',  401, {'WWW.Authentication': 'Basic realm: "Login required"'})


@app.route('/auth', methods=['GET', 'POST'])
def login_api_user():

   data = request.get_json(force=True)
   username = data.get("username")
   password = data.get("password")

   auth = request.authorization 

   if not auth or not auth.username or not auth.password:  
      return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "Login required"'})

   user = ApiUser.query.filter_by(username=auth.username).first()  
     
   if check_password_hash(user.password, auth.password):  
    #   token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
      access_token = create_access_token(identity=username, expires_delta=False, )
      return jsonify({ "token": access_token })
    #   return jsonify({'token' : token.decode('UTF-8')}) 

   return make_response('Could not verify',  401, {'WWW.Authentication': 'Basic realm: "Login required"'})


@app.route('/init_db')
def create_tables():
    try:
        import name_string_api.models.models
        db_util.db.create_all()
        print("Created successfully")
    except Exception as e:
        print("Exception occurred while creating models", e)
    return "Tables created successfully"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
