from name_string_api.database_utility import db
from flask_login import UserMixin
import enum


class RoleType(enum.Enum):
    admin = "admin"
    user = "user"


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('USERNAME', db.String(50), nullable=False)
    password = db.Column('PASSWORD', db.String(5), nullable=False)
    role = db.Column('ROLE', db.Enum(RoleType))

    def __init__(self, id, username=None, password=None, role=None):
        self.username = username
        self.password = password
        self.role = role

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": str(self.role.value),
        }
