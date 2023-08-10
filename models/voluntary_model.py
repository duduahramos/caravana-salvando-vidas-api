from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import uuid

from app import db
from dtos.voluntary_dto import VoluntaryDto
from models.blood_type_model import BloodType
from utils.utils import generate_uuid


class Voluntary(db.Model):
    __tablename__ = "voluntarys"

    id = db.Column(db.Integer, primary_key=True)
    uuid_bd = db.Column(db.BINARY(16), nullable=False, unique=True, default=generate_uuid)
    name = db.Column(db.String(60), nullable=False)
    number = db.Column(db.String(60), nullable=False)
    cpf_cnpj = db.Column(db.String(14), nullable=False)
    id_blood_type = db.Column(db.Integer, ForeignKey("blood_types.id"), nullable=True)
    blood_type_relationship = relationship("BloodType", back_populates="voluntary_relationship")

    def __init__(self, voluntary_dto: VoluntaryDto) -> None:
        self.id = None
        self.uuid_bd = None
        self.name = voluntary_dto.get("name")
        self.number = voluntary_dto.get("number")
        self.cpf_cnpj = voluntary_dto.get("cpf_cnpj")
        self.id_blood_type = voluntary_dto.get("blood_type")

    def to_dict(self):
        return {
            "id": self.id,
            # "uuid_bd": str(uuid.UUID(bytes=self.uuid_bd)),
            "name": self.name,
            "number": self.number,
            "cpf_cnpj": self.cpf_cnpj,
            "blood_type": BloodType.query.filter_by(id=self.id_blood_type).first().description
        }

    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self, name):
    #     self.name = name

    # @property
    # def number(self):
    #     return self.number

    # @number.setter
    # def number(self, number):
    #     self.number = number

    # @property
    # def cpf_cnpj(self):
    #     return self.cpf_cnpj

    # @cpf_cnpj.setter
    # def cpf_cnpj(self, cpf_cnpj):
    #     self.cpf_cnpj = cpf_cnpj

    # @property
    # def id_blood_type(self):
    #     return BloodType.query.filter_by(id=self.id_blood_type).first().description

    # @id_blood_type.setter
    # def id_blood_type(self, id_blood_type):
    #     self.id_blood_type = id_blood_type
