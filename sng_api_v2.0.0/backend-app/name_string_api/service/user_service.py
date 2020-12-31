from name_string_api.models.users import User
import name_string_api.database_utility as db_util


def get_users():
    user_list = []
    try:
        users = Users.query.with_entities(Users).all()
    except Exception as e:
        raise Exception("Error occurred while fetching users ", e)

    for user in users:
        user_list.append(user.as_dict())

    return user_list


def get_user_by_user_id(user_id):
    """
    Get user with primary key
    """
    try:
        user = Users.query.with_entities(Users)\
            .filter_by(id=user_id)\
            .one_or_none()
    except Exception as e:
        raise Exception("Failed to get a user with error", e)

    if not user:
        return "Please enter correct user_id"

    return user.as_dict()


# def add_user(user_data):
#     try:
#         user = Users(None, user_data['username'], user_data['password'],
#                      user_data['role'])
#         db_util.db.session.add(user)
#         db_util.db.session.commit()
#         db_util.db.session.close()
#     except Exception as e:
#         raise Exception("Failed to add user with error", e)

#     return "User added successfully"

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


# def validate_user(username, password):
#     user = Users.query.with_entities(Users)\
#         .filter_by(username=username)\
#         .filter_by(password=password)\
#         .one_or_none()
#     if user:
#         return user.id

#     return None


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
