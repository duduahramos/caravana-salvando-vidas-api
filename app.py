from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/voluntario/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/caravana_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)


# Controllers
from blueprints.volunteer_blueprint import volunteer_blueprint


app.register_blueprint(volunteer_blueprint)


with app.app_context():
    db.create_all()
