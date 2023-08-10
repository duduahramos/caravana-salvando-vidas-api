from flask import Blueprint, request
from marshmallow import ValidationError

from dtos.volunteer_dto import VolunteerDto
from services.volunteer_service import VolunteerService


volunteer_blueprint = Blueprint("volunteer_controller", __name__)


# REVER NECESSIDADE DO UUID
@volunteer_blueprint.route("/voluntario", methods=["POST"])
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

        return {"message": "Ocorreu um erro!"}, 500


@volunteer_blueprint.route("/voluntario", methods=["GET"])
def get_volunteers():
    try:
        volunteer_service = VolunteerService()

        volunteer_dict_list, status_code = volunteer_service.get_all()

        return volunteer_dict_list, status_code
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro!"}, 500


@volunteer_blueprint.route("/voluntario/<id>", methods=["GET"])
def get_volunteer(id):
    try:
        volunteer_service = VolunteerService()

        volunteer_dict, status_code = volunteer_service.get_one_by_id(id)

        return volunteer_dict, status_code
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro!"}, 500


@volunteer_blueprint.route("/voluntario/<id>", methods=["PUT"])
def put_volunteer(id):
    try:
        volunteer_service = VolunteerService()

        volunteer_service.update(id)
    except Exception as e:
        print(e.args)

        return{"message": "Ocorreu um erro!"}, 500
