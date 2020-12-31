from flask_sqlalchemy import SQLAlchemy
from flask_ldap3_login import LDAP3LoginManager
from name_string_api import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://svc_dbservernames:cS$807_K$a@clavipdb7820.cto1o5pr1o6l.eu-west-1.rds.amazonaws.com:5434/dbservernames'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
