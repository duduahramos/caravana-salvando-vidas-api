from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configs import config


db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/voluntario/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)
migrate = Migrate(app, db)


# Controllers
from blueprints.login_blueprint import login_blueprint
from blueprints.user_blueprint import user_blueprint
from blueprints.volunteer_blueprint import volunteer_blueprint


app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(volunteer_blueprint)


with app.app_context():
    db.create_all()
