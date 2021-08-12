from name_string_api.database_utility import db


class HostName(db.Model):
    __tablename__ = 'host_name'
    id = db.Column(db.Integer, primary_key=True)
    # service_owner = db.Column('SERVICE_OWNER', db.String(50), nullable=False)
    description = db.Column('DESCRIPTION', db.String(50), nullable=False)
    app_id = db.Column('APP_ID', db.String(50), nullable=False)
    region = db.Column('REGION', db.String(5), nullable=False)
    location = db.Column('LOCATION', db.String(10), nullable=False)
    os_name = db.Column('OS', db.String(10), nullable=False)
    zone = db.Column('ZONE', db.String(10), nullable=False)
    lifecycle = db.Column('LIFECYCLE', db.String(10), nullable=False)
    role = db.Column('ROLE', db.String(10), nullable=False)
    counter = db.Column('COUNTER', db.String(10), unique=True)

    def __init__(self, id, description, app_id, region, location, os_name, zone,
                 lifecycle, role, counter):
        #self.id = id
        # self.service_owner = service_owner
        self.description = description
        self.app_id = app_id
        self.region = region
        self.location = location
        self.os_name = os_name
        self.zone = zone
        self.lifecycle = lifecycle
        self.role = role
        self.counter = counter

    def as_dict(self):
        return {
            "id": self.id,
            # "service_owner": self.service_owner,
            "description": self.description,
            "app_id": self.app_id,
            "region": self.region,
            "location": self.location,
            "os": self.os_name,
            "zone": self.zone,
            "lifecycle": self.lifecycle,
            "role": self.role,
            "counter": self.counter
        }

# db.create_all()
