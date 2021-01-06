from name_string_api.database_utility import db
from flask_login import UserMixin
import enum


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    username = db.Column('USERNAME', db.String(50), nullable = False)

    def __init__(self, username=None, public_id=None):
        self.username = username
        self.public_id = public_id

    def as_dict(self):
        return {
            "username": self.username,
            "public_id": self.public_id,
        }
