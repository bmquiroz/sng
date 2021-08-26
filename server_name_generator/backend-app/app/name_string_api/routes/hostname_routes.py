from name_string_api import app, api
from flask_restful import Resource
from name_string_api.models.hostnames import HostName
from flask import render_template, request, redirect, url_for, jsonify, make_response
from name_string_api.service import hostname_service as hostname_svc
from flask_cors import CORS, cross_origin
import json
import logging
logging.getLogger('flask_cors').setLevel(logging.DEBUG)
logging.basicConfig()
from flask_jwt_extended import jwt_required, get_jwt_identity


CORS(app)
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/get_hostnames', methods=['POST', 'GET'])
@cross_origin()
def get_hostnames():
    if request.method == 'POST':
        results = HostName.query.with_entities(HostName).all()
        result_list = []
        if results:
            for result in results:
                name_string = '{}{}{}{}{}{}{}'.format(result.region,
                                                      result.location,
                                                      result.os_name,
                                                      result.zone,
                                                      result.lifecycle,
                                                      result.role,
                                                      result.counter)
                data = dict(region=result.region,
                            description=result.description,
                            app_id=result.app_id,
                            hostname=name_string)

                result_list.append(data)
        response = make_response(json.dumps(result_list), 200)
        return response


@app.route('/hostname/<host_id>', methods=['DELETE'])
def delete_hostname(host_id):
    msg = ""
    try:
        msg = hostname_svc.delete_hostname(host_id)
    except Exception as e:
        print("Exception occurred while deleting hostname with error", e)
    return msg


@app.route('/add_host', methods=['POST', 'GET'])
def add_host():
    return render_template('add_host.html')


@app.route('/query_host', methods=['POST', 'GET'])
def query_host():
    return render_template('query_host.html')


@app.route('/api/create_string', methods=['POST', 'GET'])
def create_sting():
    if request.method == 'POST':
        hostname_string = hostname_svc.insert_hostname(request.form)
        response = make_response(jsonify({"host_name": hostname_string}), 200)
        response.headers.add('Access-Control-Allow-Origin', 'http://sng.home.redchip.net')
        return response


@app.route('/create_hostname', methods=['POST', 'GET'])
@jwt_required
def create_hostname():
    if request.method == 'POST':
        data = request.get_json(force=True)

        hostname_string = hostname_svc.insert_hostname(data)

        return {"hostname": hostname_string}


# @app.route('/create_hostname', methods=['POST', 'GET'])
# @jwt_required
# def create_hostname():
#     if request.method == 'POST':
#         data_list = request.get_json(force=True)

#         # data_list = {data}

#         hostname_string = hostname_svc.insert_hostname(data_list)

#         return {"hostname": hostname_string}


# @app.route('/create_hostname', methods=['POST', 'GET'])
# @jwt_required
# def create_hostname():
#     if request.method == 'POST':
#         data = request.get_json(force=True)

#         data_list = [data]

#         hostname_string = hostname_svc.insert_hostname(data_list)

#         return {"hostname": hostname_string}
        

# @app.route('/create_hostname', methods=['POST', 'GET'])
# @jwt_required
# def create_hostname():
#     if request.method == 'POST':
#         data = request.get_json(force=True)
#         hostname_string = hostname_svc.insert_hostname(data)

#         return {"hostname": hostname_string}


@app.route('/query_ad/<hostname>', methods=['POST', 'GET'])
@jwt_required
def query_ad(hostname):
    if request.method == 'POST':
        data = request.get_json(force=True)
        ldap_object_query = hostname_svc.query_hostname_ad(hostname)

        return ldap_object_query
