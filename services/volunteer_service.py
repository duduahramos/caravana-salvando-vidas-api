from flask import request
from sqlalchemy import desc

from app import db
from schemas.volunteer_schema import VolunteerSchema
from models.volunteer_model import Volunteer as VolunteerModel


class VolunteerService:
    def __init__(self) -> None:
        pass

    def save(self, volunteer_schema: VolunteerSchema) -> VolunteerModel:
        volunteer_model = VolunteerModel(volunteer_schema)

        db.session.add(volunteer_model)
        db.session.commit()

        return volunteer_model.to_dict()

    def update(self, id: str) -> list:
        volunteer_json = request.get_json()
        volunteer_schema = VolunteerSchema().load(volunteer_json)

        volunteer_model = VolunteerModel.query.filter_by(id=id).first()
        if volunteer_model:
            volunteer_model.name = volunteer_schema.get("name")
            volunteer_model.number = volunteer_schema.get("number")
            volunteer_model.cpf_cnpj = volunteer_schema.get("cpf_cnpj")
            volunteer_model.blood_type = volunteer_schema.get("blood_type")

            db.session.commit()

            return volunteer_model.to_dict(), 202
        else:
            volunteer_model = VolunteerModel(volunteer_schema)

            db.session.add(volunteer_model)
            db.session.commit()

            return volunteer_model.to_dict(), 201

    def delete(self, id: str) -> list:
        volunteer_model = VolunteerModel.query.filter_by(id=id).first()

        if volunteer_model:
            db.session.delete(volunteer_model)
            db.session.commit()

            return [{"message": "Registro deletado."}, 200]
        else:
            return [{"message": "Registro não localizado."}, 404]

    def get_all(self) -> dict:
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=20, type=int)
        order_by = request.args.get("order_by", default="id", type=str)
        orientation = request.args.get("orientation", default="asc", type=str).upper()
        search_field = request.args.get("search_field", default="", type=str).upper()
        search = request.args.get("search", default="", type=str).upper()

        if orientation == "DESC":
            order_clause = desc(order_by)
        else:
            order_clause = order_by

        if search_field == "ID":
            field = VolunteerModel.id
        elif search_field == "NAME":
            field = VolunteerModel.name
        elif search_field == "NUMBER":
            field = VolunteerModel.number
        elif search_field == "CPF_CNPJ":
            field = VolunteerModel.cpf_cnpj
        elif search_field == "BLOOD_TYPE":
            field = VolunteerModel.id_blood_type
        elif search_field == "CREATED_ON":
            field = VolunteerModel.created_on
        else:
            field = None

        if field:
            volunteers_list = db.paginate(VolunteerModel.query.filter(field.like(f"%{search}%")).order_by(order_clause), page=page, per_page=per_page)
        else:
            volunteers_list = db.paginate(VolunteerModel.query.order_by(order_clause), page=page, per_page=per_page)

        volunteers_dict_list = {
            "items_total": volunteers_list.total,
            "pages_total": volunteers_list.pages,
            "items_current_page": len(volunteers_list.items),
            "current_page": volunteers_list.page
        }

        volunteers_dict_list["voluntarios"] = [volunteer.to_dict() for volunteer in volunteers_list]

        return volunteers_dict_list

    def get_one_by_id(self, id: str) -> dict:
        volunteer_model = VolunteerModel.query.filter_by(id=id).first()

        if volunteer_model:
            return volunteer_model.to_dict()
        else:
            return {"message": "Registro não localizado."}

    # def get_by_uuid_bd(self, uuid_bytes: bytes) -> VolunteerModel:
    #     volunteer_model = VolunteerModel.query.filter_by(uuid_bd=uuid_bytes).first()

    #     return volunteer_model
