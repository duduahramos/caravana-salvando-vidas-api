from flask import Blueprint, request
from marshmallow import ValidationError

from dtos.voluntary_dto import VoluntaryDto
from services.voluntary_service import VoluntaryService


voluntary_blueprint = Blueprint("voluntary_print", __name__)


@voluntary_blueprint.route("/voluntario", methods=["POST"])
def post_voluntary():
    voluntary_json = request.get_json()

    try:
        voluntary_dto = VoluntaryDto().load(voluntary_json)

        voluntary_service = VoluntaryService()
        voluntary_dict = voluntary_service.save(voluntary_dto)

        return voluntary_dict, 201, {"teste_header_response": "123"}
    except ValidationError as e:
        print("BODY REQUEST INVÁLIDO!")
        print(e.args)
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@voluntary_blueprint.route("/voluntario", methods=["GET"])
def get_voluntarys():
    try:
        voluntary_service = VoluntaryService()

        voluntary_dict_list, status_code = voluntary_service.get_all()

        return voluntary_dict_list, status_code, {"teste_header_response": "123"}
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@voluntary_blueprint.route("/voluntario/<id>", methods=["GET"])
def get_voluntary(id):
    try:
        voluntary_service = VoluntaryService()

        voluntary_dict, status_code = voluntary_service.get_one_by_id(id)

        return voluntary_dict, status_code, {"teste_header_response": "123"}
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@voluntary_blueprint.route("/voluntario/<id>", methods=["PUT"])
def put_voluntary(id):
    try:
        voluntary_service = VoluntaryService()

        voluntary_service.update()
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500
