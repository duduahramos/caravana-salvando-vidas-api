from flask import Blueprint, request
from marshmallow import ValidationError

from schemas.volunteer_schema import VolunteerSchema
from services.volunteer_service import VolunteerService


volunteer_blueprint = Blueprint("volunteer_blueprint", __name__)


@volunteer_blueprint.route("/voluntario", methods=["POST"])
def post_volunteer():
    volunteer_json = request.get_json()

    try:
        volunteer_schema = VolunteerSchema().load(volunteer_json)

        volunteer_service = VolunteerService()
        volunteer_dict = volunteer_service.save(volunteer_schema)

        return volunteer_dict, 201
    except ValidationError as e:
        print(e.args)

        return {"message": "Corpo da requisação inválido."}, 400
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@volunteer_blueprint.route("/voluntario", methods=["GET"])
def get_all_volunteers():
    try:
        volunteer_service = VolunteerService()

        volunteer_dict_list = volunteer_service.get_all()

        return volunteer_dict_list, 200
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@volunteer_blueprint.route("/voluntario/<id>", methods=["GET"])
def get_one_volunteer(id):
    try:
        volunteer_service = VolunteerService()

        volunteer_dict, status_code = volunteer_service.get_one_by_id(id)

        return volunteer_dict, 200
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@volunteer_blueprint.route("/voluntario/<id>", methods=["PUT"])
def put_volunteer(id):
    try:
        volunteer_service = VolunteerService()

        volunteer_dict, status_code = volunteer_service.update(id)

        return volunteer_dict, status_code
    except ValidationError as e:
        print(e.args)

        return {"message": "Corpo da requisação inválido."}, 500
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@volunteer_blueprint.route("/voluntario/<id>", methods=["DELETE"])
def delete_volunteer(id):
    try:
        volunteer_service = VolunteerService()

        volunteer_dict, status_code = volunteer_service.delete(id)

        return volunteer_dict, status_code
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500
