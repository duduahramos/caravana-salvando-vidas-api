from flask import Blueprint, request
from marshmallow import ValidationError

from schemas.user_schema import UserSchema
from services.login_service import LoginService


login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route("/login", methods=["POST"])
def login():
    login_json = request.get_json()

    try:
        user_schema = UserSchema.load(login_json)

        login_service = LoginService()
        login_json_response = login_service.login()

    except ValidationError as e:
        print(e.args)

        return {"message": e.args}, 400
    except Exception as e:
        print(e.args)

        return {"message": "Ocorreu um erro."}, 500
