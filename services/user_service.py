from flask import request

from app import db
from models.user_model import UserModel


class UserService:
    def __init__(self) -> None:
        pass

    def save(self, user_schema):
        user_model = UserModel(user_schema)

        db.session.add(user_model)
        db.session.commit()

        return user_model.to_dict()

    def get_all(self):
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=20, type=int)

        users_list = db.paginate(UserModel.query.order_by("id"), page=page, per_page=per_page)

        users_dict_list = {
            "items_total": users_list.total,
            "pages_total": users_list.pages,
            "items_current_page": len(users_list.items),
            "current_page": users_list.page
        }

        users_dict_list["users"] = [user.to_dict() for user in users_list]

        return users_dict_list

    def delete(self, id):
        user_model = UserModel.query.filter_by(id=id).first()

        db.session.delete(user_model)
        db.session.commit()
