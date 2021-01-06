from flask_sqlalchemy import SQLAlchemy
from flask_ldap3_login import LDAP3LoginManager
from name_string_api import app
import os


base_uri = os.environ['SQLALCHEMY_DATABASE_URI']


app.config['SQLALCHEMY_DATABASE_URI'] = base_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
