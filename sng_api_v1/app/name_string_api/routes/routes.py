from name_string_api import app
from name_string_api.models.users import Users
import name_string_api.database_utility as db_util
from name_string_api.service import user_service as user_svc
from flask import render_template, request, redirect, url_for, abort, Response
from flask_login import LoginManager, UserMixin, login_required, login_user,\
    logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return Users(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = user_svc.validate_user(username, password)

        if user_id:
            role = user_svc.get_role(user_id)
            user = Users(user_id)
            login_user(user)
            if role.lower() == 'admin':
                return redirect(url_for('index'))
            else:
                return redirect(url_for(''))
    return render_template('login.html')


@app.route('/', methods=['POST', 'GET'])
@login_required
def index():
    print("Admin User")
    return render_template('index.html')


@app.route('/use')
@login_required
def index1():
    print("Normal User")
    return render_template('admin_index.html')


@app.route('/init_db')
def create_tables():
    try:
        import name_string_api.models.models
        db_util.db.create_all()
        print("Created successfully")
    except Exception as e:
        print("Exception occurred while creating models", e)
    return "Tables created successfully"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')



