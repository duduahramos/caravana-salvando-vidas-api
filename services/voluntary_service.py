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

        return voluntary_model.voluntary_to_dict()

    def get_by_uuid_bd(self, uuid_bytes: bytes) -> VoluntaryModel:
        voluntary_model = VoluntaryModel.query.filter_by(uuid_bd=uuid_bytes).first()

        return voluntary_model
