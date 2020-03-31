from flask_sqlalchemy import SQLAlchemy
from name_string_api import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:pass@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
