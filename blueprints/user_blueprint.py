from flask import Blueprint, request
from marshmallow import ValidationError
from sqlalchemy import exc

from schemas.user_schema import UserSchema
from services.user_service import UserService


user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route("/usuario", methods=["POST"])
def post_user():
    user_json = request.get_json()

    try:
        user_schema = UserSchema().load(user_json)

        user_service = UserService()
        user_dict = user_service.save(user_schema)

        return user_dict, 201
    except ValidationError as e:
        print(e.args)

        return {"message": "Corpo da requisição inválido."}, 400
    except exc.IntegrityError as e:
        print(e.args)

        return {"message": e.orig.args[1]}, 400
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@user_blueprint.route("/usuario", methods=["GET"])
def get_all_users():
    try:
        user_service = UserService()
        users_dict_list = user_service.get_all()

        return users_dict_list, 201
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500


@user_blueprint.route("/usuario/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        user_service = UserService()
        user_service.delete(id)

        return {"message": "Usuário deletado."}, 200
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500

