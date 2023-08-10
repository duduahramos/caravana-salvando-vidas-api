from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/caravana_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)


# Models
from models.volunteer_model import Volunteer as VolunteerModel
from models.blood_type_model import BloodType as BloodTypeModel

# Controllers
from blueprints.volunteer_blueprint import volunteer_blueprint


app.register_blueprint(volunteer_blueprint)


with app.app_context():
    db.create_all()


@app.route("/hello_world")
def hello_world():
    return {"message": "Hello Caravana!"}
