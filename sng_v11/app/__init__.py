from flask import Flask
# from sqlalchemy.dialects.mysql import BIGINT
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os


app = Flask(__name__)
app.secret_key = 'super secret key'
tmp = tempfile.gettempdir()
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(FILE_PATH, "data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


from app import routes