from sqlalchemy.orm import relationship

from app import db


class BloodType(db.Model):
    __tablename__ = "blood_types"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(10), nullable=False)
    volunteer_relationship = relationship("Volunteer", back_populates="blood_type_relationship")
