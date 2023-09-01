from flask import Blueprint, request
from marshmallow import ValidationError

from schemas.login_schema import LoginSchema
from services.login_service import LoginService
from errors.login_errors import IncorrectPassword
from errors.user_errors import UserNotFound


login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route("/login", methods=["POST"])
def login():
    try:
        if not request.data:
            return {"message": "Corpo de requisição inválido."}, 400

        login_json = request.get_json()
        login_schema = LoginSchema().load(login_json)

        login_service = LoginService()
        # user_model = login_service.get_user_by_user_name(login_schema)
        login_json_response, status_code = login_service.login(login_schema)

        return login_json_response, status_code
    except IncorrectPassword as e:
        print(e)

        return {"message": "Senha incorreta."}, 401
    except UserNotFound as e:
        print(e)

        return {"message": "Usuário não localizado."}, 404
    except ValidationError as e:
        print(e)

        return {"message": e.args}, 400
    except Exception as e:
        print(e)

        return {"message": "Ocorreu um erro."}, 500
