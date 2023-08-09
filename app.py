from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import ValidationError

from dtos.voluntary_dto import VoluntaryDto


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/caravana_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate = Migrate(app, db)


from models.voluntary_model import Voluntary as VoluntaryModel
from models.blood_type_model import BloodType as BloodTypeModel
from services.voluntary_service import VoluntaryService


with app.app_context():
    db.create_all()


@app.route("/hello_world")
def hello_world():
    return {"message": "Hello Caravana!"}


# REVER NECESSIDADE DO UUID
@app.route("/voluntario", methods=["POST"])
def post_voluntary():
    voluntary_json = request.get_json()

    try:
        voluntary_dto = VoluntaryDto().load(voluntary_json)

        voluntary_service = VoluntaryService()
        voluntary_dict = voluntary_service.save(voluntary_dto)

        return voluntary_dict, 201, {"teste": "123"}
    except ValidationError as e:
        print(e.args)

    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro!"}
