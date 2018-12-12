from flask import render_template, redirect, request, url_for
from app import app
from app import db
import random
from app.hostnames import HostName


@app.route('/add_host', methods=['POST', 'GET'])
def add_host():
    return render_template('add_host.html')

@app.route('/query_host', methods=['POST', 'GET'])
def query_host():
    return render_template('query_host.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


def get_region_abbreviations(region):
    regions = ['NA', 'APAC', 'EMEA', 'LATAM']
    if region in regions:
        if region == 'NA':
            region = 'N'
        elif region == 'APAC':
            region = 'A'
        elif region == 'EMEA':
            region = 'E'
        elif region == 'LATAM':
            region = 'S'
    return region


def get_location_abbreviations(location):
    locations = ['AWS Cloud', 'Wynyard', 'Frankfurt', 'Atlanta']
    if location in locations:
        if location == 'AWS Cloud':
            location = 'CLA'
        elif location == 'Wynyard':
            location = 'WYN'
        elif location == 'Frankfurt':
            location = 'FRK'
        elif location == 'Atlanta':
            location = 'ATL'
    return location


def get_os_name_abbreviations(os_name):
    os_names = ['RedHat', 'Windows', 'SLES', 'Other Linux']
    if os_name in os_names:
        if os_name == 'RedHat':
            os_name = 'V'
        elif os_name == 'Windows':
            os_name = 'W'
        elif os_name == 'SLES':
            os_name = 'L'
        elif os_name == 'Other Linux':
            os_name = 'X'

    return os_name


def get_zone_abbreviations(zone):
    zones = ['Non-DMZ', 'DMZ']
    if zone in zones:
        if zone == 'Non-DMZ':
            zone = 'N'
        elif zone == 'DMZ':
            zone = 'D'

    return zone


def get_lifecycle_abbreviations(lifecycle):
    lifecycles = ['Proof of Concept', 'Lab', 'Development', 'Test Quality Assurance', 'Stress Performance Load Testing', 'Quality Control UAT Pre-Prod Staging', 'Production']

    if lifecycle in lifecycles:
        if lifecycle == 'Proof of Concept':
            lifecycle = 'I'
        elif lifecycle == 'Lab':
            lifecycle = 'L'
        elif lifecycle == 'Development':
            lifecycle = 'D'
        elif lifecycle == 'Test Quality Assurance':
            lifecycle = 'T'
        elif lifecycle == 'Stress Performance Load Testing':
            lifecycle = 'S'
        elif lifecycle == 'Quality Control UAT Pre-Prod Staging':
            lifecycle = 'Q'
        elif lifecycle == 'Production':
            lifecycle = 'P'

    return lifecycle


def get_role_abbreviations(role):
    roles = ['Web', 'Database Oracle', 'Database SQL Server', 'Database MySQL', 'Database Mongo', 'Database DB2', 'Database Postgres', 'Database Hadoop', 'Application', 'Backup', 'Management Monitoring', 'Hypervisor', 'Citrix', 'DWR Domain Controller', 'RO Domain Controller', 'LDAP', 'Google Appliance', 'File Server', 'Witness', 'Config Mgr Site Server', 'Config Mgr Dist Point', 'Config Mgr Mgt Point', 'Config Mgr Cloud Dis Point', 'Config Mgr Cloud Proxy', 'Config Mgr IBCM']

    if role in roles:
        if role == 'Web':
            role = 'WEB'
        elif role == 'Database Oracle':
            role = 'DBO'
        elif role == 'Database SQL Server':
            role = 'DBS'
        elif role == 'Database MySQL':
            role = 'DBM'
        elif role == 'Database Mongo':
            role = 'DBG'
        elif role == 'Database DB2':
            role = 'DB2'
        elif role == 'Database Postgres':
            role = 'DBP'
        elif role == 'Database Hadoop':
            role = 'DBH'
        elif role == 'Application':
            role = 'APP'
        elif role == 'Backup':
            role = 'BKP'
        elif role == 'Management Monitoring':
            role = 'MGT'
        elif role == 'Hypervisor':
            role = 'HYP'
        elif role == 'Citrix':
            role = 'CTX'
        elif role == 'DWR Domain Controller':
            role = 'ADC'
        elif role == 'RO Domain Controller':
            role = 'ADO'
        elif role == 'LDAP':
            role = 'LDP'
        elif role == 'Google Appliance':
            role = 'GAP'
        elif role == 'File Server':
            role = 'FLS'
        elif role == 'Witness':
            role = 'WIT'
        elif role == 'Config Mgr Site Server':
            role = 'CMS'
        elif role == 'Config Mgr Dist Point':
            role = 'CMD'
        elif role == 'Config Mgr Mgt Point':
            role = 'CMM'
        elif role == 'Config Mgr Cloud Dis Point':
            role = 'CMC'
        elif role == 'Config Mgr Cloud Proxy':
            role = 'CMP'
        elif role == 'Config Mgr IBCM':
            role = 'CMI'

    return role


@app.route('/create_string', methods=['POST', 'GET'])
def create_string():
    if request.method == 'POST':
        service_owner = request.form['service_owner']
        region = request.form['region']
        location = request.form['location']
        os_name = request.form['os']
        zone = request.form['zone']
        lifecycle = request.form['lifecycle']
        role = request.form['role']
        counter = random.randint(00000, 99999)
        region = get_region_abbreviations(region)
        location = get_location_abbreviations(location)
        os_name = get_os_name_abbreviations(os_name)
        zone = get_zone_abbreviations(zone)
        lifecycle = get_lifecycle_abbreviations(lifecycle)
        role = get_role_abbreviations(role)
        hostname_string = region + location + os_name + zone +lifecycle + \
                          role + str(counter)
        hostname = HostName(service_owner, region, location, os_name
                                      , zone, lifecycle, role,  counter)
        db.session.add(hostname)
        db.session.commit()
        db.session.close()
        return render_template('add_host.html', name_string=hostname_string)


@app.route('/get_hostnames', methods=['POST', 'GET'])
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
                data = dict(region=result.region, service_owner=result.service_owner, hostname=name_string)
                result_list.append(data)

        return render_template('query_host.html', results=result_list)
    return redirect(url_for('query_host'))
