from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import ValidationError

from dtos.volunteer_dto import VolunteerDto


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/caravana_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)


from models.volunteer_model import Volunteer as VolunteerModel
from models.blood_type_model import BloodType as BloodTypeModel
from services.volunteer_service import VolunteerService


with app.app_context():
    db.create_all()


@app.route("/hello_world")
def hello_world():
    return {"message": "Hello Caravana!"}


# REVER NECESSIDADE DO UUID
@app.route("/voluntario", methods=["POST"])
def post_volunteer():
    volunteer_json = request.get_json()

    try:
        volunteer_dto = VolunteerDto().load(volunteer_json)

        volunteer_service = VolunteerService()
        volunteer_dict = volunteer_service.save(volunteer_dto)

        return volunteer_dict, 201, {"teste": "123"}
    except ValidationError as e:
        print(e.args)

    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro!"}
