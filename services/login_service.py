from models.user_model import UserModel
from utils.auth import auth


class LoginService:
    def __init__(self) -> None:
        pass

    def login(self, login_schema):
        user_model = self.get_user_by_email(login_schema)
        if user_model:
            pass

    def get_user_by_email(self, login_schema):
        user_model = UserModel.query.filter_by(email=login_schema.get("email")).first()

        return user_model
