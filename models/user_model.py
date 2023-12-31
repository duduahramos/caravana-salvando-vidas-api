from datetime import datetime
# from werkzeug.security import generate_password_hash

from app import db
from utils.utils import generate_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    admin = db.Column(db.Integer, nullable=False, default=0)
    created_on = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, user_schema_teste) -> None:
        self.id = None
        self.name = user_schema_teste.get("name")
        self.user_name = user_schema_teste.get("user_name")
        self.admin = None
        self.password = generate_password_hash(user_schema_teste.get("password"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_name": self.user_name,
            "admin": self.admin,
            "created_on": datetime.strftime(self.created_on, "%H:%M:%S %d/%m/%Y")
        }
