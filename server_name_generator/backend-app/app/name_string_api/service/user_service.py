from name_string_api.models.users import User
from name_string_api.models.users import ApiUser
import name_string_api.database_utility as db_util
import uuid 


def add_api_user(user_data):
    try:
        user = ApiUser(None, user_data['username'], user_data['password'])
        db_util.db.session.add(user)
        db_util.db.session.commit()
        db_util.db.session.close()
    except Exception as e:
        raise Exception("Failed to add user with error", e)

    return "API user added successfully"


# def add_api_user(user_data):
#     try:
#         user = ApiUser(None, public_id=str(uuid.uuid4()), user_data['username'], user_data['password'])
#         db_util.db.session.add(user)
#         db_util.db.session.commit()
#         db_util.db.session.close()
#     except Exception as e:
#         raise Exception("Failed to add user with error", e)

#     return "API user added successfully"


def validate_api_user(username, password):
    user = ApiUser.query.with_entities(ApiUser)\
        .filter_by(username=username)\
        .filter_by(password=password)\
        .one_or_none()
    if user:
        return user.id

    return None


def add_user(user_data):
    user = User(None, user_data('username'))
    db_util.db.session.add(user) 
    db_util.db.session.commit()
    db_util.db.session.close()
    return user_data


def validate_user(username):
    user = User.query.with_entities(User)\
        .filter_by(username=username)\
        .one_or_none()
    if user:
        return user.id

    return None
