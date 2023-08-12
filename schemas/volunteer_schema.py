from marshmallow import Schema, fields, validate


class VolunteerSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_messages={"error_message": "Name is required."})
    number = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_messages={"error_message": "Number is required."})
    cpf_cnpj = fields.Str(required=True, validate=validate.Length(min=0, max=14), error_messages={"error_message": "CPF/CNPJ is required."})
    blood_type = fields.Int(required=True, error_messages={"error_message": "Blood type is required."})
