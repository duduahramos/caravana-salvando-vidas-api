from flask import request
from typing import List

from app import db
from dtos.voluntary_dto import VoluntaryDto
from models.voluntary_model import Voluntary as VoluntaryModel


class VoluntaryService:
    def __init__(self) -> None:
        pass

    def save(self, voluntary_dto: VoluntaryDto) -> VoluntaryModel:
        voluntary_model = VoluntaryModel(voluntary_dto)

        db.session.add(voluntary_model)
        db.session.commit()

        return voluntary_model.to_dict()

    def update(self, id: str) -> VoluntaryModel:
        voluntary_model = VoluntaryModel.query.filter_by(id=id).first()

        if voluntary_model:
            voluntary_json = request.get_json()
            voluntary_dto = VoluntaryDto().load(voluntary_json)

            voluntary_model.name = voluntary_dto.name
            voluntary_model.number = voluntary_dto.number
            voluntary_model.cpf_cnpj = voluntary_dto.cpf_cnpj
            voluntary_model.blood_type = voluntary_dto.blood_type

            print("TESTE")

    def get_all(self) -> list:
        voluntary_list = VoluntaryModel.query.order_by(VoluntaryModel.id).all()

        voluntary_dict_list = {}

        voluntary_dict_list["voluntarios"] = [x.to_dict() for x in voluntary_list]

        if voluntary_list:
            status_code = 200
        else:
            status_code = 404

        return [voluntary_dict_list, status_code]

    def get_one_by_id(self, id: str) -> list:
        voluntary_model = VoluntaryModel.query.filter_by(id=id).first()

        if voluntary_model:
            return [voluntary_model.to_dict(), 200]
        else:
            return [{}, 404]

    # def get_by_uuid_bd(self, uuid_bytes: bytes) -> VoluntaryModel:
    #     voluntary_model = VoluntaryModel.query.filter_by(uuid_bd=uuid_bytes).first()

    #     return voluntary_model
