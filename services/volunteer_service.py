from flask import request
from typing import List

from app import db
from dtos.volunteer_dto import VolunteerDto
from models.volunteer_model import Volunteer as VolunteerModel


class VolunteerService:
    def __init__(self) -> None:
        pass

    def save(self, volunteer_dto: VolunteerDto) -> VolunteerModel:
        volunteer_model = VolunteerModel(volunteer_dto)

        db.session.add(volunteer_model)
        db.session.commit()

        return volunteer_model.to_dict()

    def update(self, id: str) -> VolunteerModel:
        volunteer_model = VolunteerModel.query.filter_by(id=id).first()

        if volunteer_model:
            volunteer_json = request.get_json()
            volunteer_dto = VolunteerDto().load(volunteer_json)

            volunteer_model.name = volunteer_dto.name
            volunteer_model.number = volunteer_dto.number
            volunteer_model.cpf_cnpj = volunteer_dto.cpf_cnpj
            volunteer_model.blood_type = volunteer_dto.blood_type

            print("TESTE")

    def get_all(self) -> list:
        volunteer_list = VolunteerModel.query.order_by(VolunteerModel.id).all()

        volunteer_dict_list = {}

        volunteer_dict_list["voluntarios"] = [x.to_dict() for x in volunteer_list]

        if volunteer_list:
            status_code = 200
        else:
            status_code = 404

        return [volunteer_dict_list, status_code]

    def get_one_by_id(self, id: str) -> list:
        volunteer_model = VolunteerModel.query.filter_by(id=id).first()

        if volunteer_model:
            return [volunteer_model.to_dict(), 200]
        else:
            return [{}, 404]

    # def get_by_uuid_bd(self, uuid_bytes: bytes) -> VolunteerModel:
    #     volunteer_model = VolunteerModel.query.filter_by(uuid_bd=uuid_bytes).first()

    #     return volunteer_model
