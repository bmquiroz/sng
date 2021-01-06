from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.secret_key = 'super secret key'

import name_string_api.routes.routes
import name_string_api.routes.user_routes
import name_string_api.routes.hostname_routes
