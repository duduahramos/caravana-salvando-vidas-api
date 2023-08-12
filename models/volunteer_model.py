from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime

from app import db
from schemas.volunteer_schema import VolunteerSchema
from models.blood_type_model import BloodType
from utils.utils import generate_uuid


class Volunteer(db.Model):
    __tablename__ = "volunteers"

    id = db.Column(db.Integer, primary_key=True)
    uuid_bd = db.Column(db.BINARY(16), nullable=False, unique=True, default=generate_uuid)
    name = db.Column(db.String(60), nullable=False)
    number = db.Column(db.String(60), nullable=False)
    cpf_cnpj = db.Column(db.String(14), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now())
    id_blood_type = db.Column(db.Integer, ForeignKey("blood_types.id"), nullable=True)
    blood_type_relationship = relationship("BloodType", back_populates="volunteer_relationship")

    def __init__(self, volunteer_schema: VolunteerSchema) -> None:
        self.id = None
        self.uuid_bd = None
        self.name = volunteer_schema.get("name")
        self.number = volunteer_schema.get("number")
        self.cpf_cnpj = volunteer_schema.get("cpf_cnpj")
        self.id_blood_type = volunteer_schema.get("blood_type")

    def to_dict(self):
        return {
            "id": self.id,
            # "uuid_bd": str(uuid.UUID(bytes=self.uuid_bd)),
            "name": self.name,
            "number": self.number,
            "cpf_cnpj": self.cpf_cnpj,
            "created_on": datetime.strftime(self.created_on, "%H:%M:%S %d/%m/%Y"),
            "blood_type": BloodType.query.filter_by(id=self.id_blood_type).first().description
        }
