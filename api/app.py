from flask import Flask
from user.views import user_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.config.DevelopmentConfig')
CORS(app, origins='http://localhost:8080')
app.register_blueprint(user_blueprint, url_prefix='/auth')
