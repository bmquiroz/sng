from name_string_api.models.hostnames import HostName
import name_string_api.database_utility as db_util


def get_values_for_hostname(data):
    """
    :param data: description, app_id, region, location, os, lifecycle, role
    :return: abbreviated value of description, app_id, region, location, os,
            lifecycle, role
    """
    try:
        hostname = HostName.query\
            .with_entities(HostName.counter)\
            .order_by(HostName.id.desc())\
            .first()
    except Exception as e:
        raise Exception('Failed to get hostname with error: ', e)

    if hostname:
        counter = hostname.counter
        counter = str(int(counter) + 1)
    else:
        counter = 0
        counter += 1
        counter = str(counter)
    if counter:
        counter = '%05d' % (int(counter))

    # service_owner = data['service_owner']
    description = data['description']
    app_id = data['app_id']
    region = data['region']
    location = data['location']
    os_name = data['os']
    zone = data['zone']
    lifecycle = data['lifecycle']
    role = data['role']
    region = get_region_abbreviations(region)
    location = get_location_abbreviations(location)
    os_name = get_os_name_abbreviations(os_name)
    zone = get_zone_abbreviations(zone)
    lifecycle = get_lifecycle_abbreviations(lifecycle)
    role = get_role_abbreviations(role)

    return description, app_id, region, location, os_name, zone, lifecycle, role,\
        counter


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
    locations = ['AWS Cloud', 'Azure Cloud', 'Wynyard', 'Frankfurt', 'Atlanta']
    if location in locations:
        if location == 'AWS Cloud':
            location = 'CLA'
        elif location == 'Azure Cloud':
            location = 'CLM'
        elif location == 'Private Cloud':
            location = 'CLP'
        elif location == 'Wynyard':
            location = 'WYN'
        elif location == 'Frankfurt':
            location = 'FRK'
        elif location == 'Atlanta':
            location = 'ATL'
    return location


def get_os_name_abbreviations(os_name):
    os_names = ['Red Hat', 'Windows', 'SLES', 'Other Linux']
    if os_name in os_names:
        if os_name == 'Red Hat':
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


def insert_hostname(data):
    description, app_id, region, location, os_name, zone, lifecycle, role, \
        counter = get_values_for_hostname(data)
    hostname_string = region + location + os_name + zone + lifecycle + \
                      role + str(counter)
    hostname_data = HostName(None, description, app_id, region, location, os_name, zone, lifecycle, role, counter)
    db_util.db.session.add(hostname_data)
    db_util.db.session.commit()
    db_util.db.session.close()
    return hostname_string


def delete_hostname(host_id):
    try:
        host_name = HostName.query.filter_by(id=host_id).one_or_none()
        if host_name:
            db_util.db.session.delete(host_name)
            db_util.db.session.commit()
            db_util.db.session.close()

            return "Deleted successfully"
        else:
            return 'Invalid host ID'

    except Exception as e:
        raise Exception("Error occurred while deleting hostname with error: ", e)
