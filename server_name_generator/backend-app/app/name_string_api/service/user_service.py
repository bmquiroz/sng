from name_string_api.models.users import User
from name_string_api.models.users import ApiUser
import name_string_api.database_utility as db_util


def add_api_user(user_data):
    try:
        user = ApiUser(None, user_data['username'], user_data['password'])
        db_util.db.session.add(user)
        db_util.db.session.commit()
        db_util.db.session.close()
    except Exception as e:
        raise Exception("Failed to add user with error", e)

    return "API user added successfully"


def add_user(user_data):
    user = User(None, user_data('username'))
    db_util.db.session.add(user) 
    db_util.db.session.commit()
    db_util.db.session.close()
    return user_data
    

def delete_user(user_id):
    """
    Delete user by its primary key id
    """
    try:
        user = Users.query.filter_by(id=user_id).one()
        db_util.db.session.delete(user)
        db_util.db.session.commit()
        db_util.db.session.close()
    except Exception as e:
        raise Exception("Failed to delete user with error", e)

    return user


def validate_user(username):
    user = User.query.with_entities(User)\
        .filter_by(username=username)\
        .one_or_none()
    if user:
        return user.id

    return None


def get_role(user_id):
    try:
        role = Users.query.with_entities(Users.role)\
            .filter_by(id=user_id)\
            .one_or_none()
        print(str(role[0].value))

        if not role:
            return "Failed to get role for user {}".format(user_id)

    except Exception as e:
        raise Exception("Failed to get role for user with user_id {} with error ()".format(user_id, str(e)))

    return str(role[0].value)
