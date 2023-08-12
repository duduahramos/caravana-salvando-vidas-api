from marshmallow import Schema, fields, validate


class VolunteerDto(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_messages={'required': 'Name is required.'})
    number = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_messages={'required': 'Number is required.'})
    cpf_cnpj = fields.Str(required=True, validate=validate.Length(min=0, max=14), error_messages={'required': 'CPF/CNPJ is required.'})
    blood_type = fields.Int(required=True, error_messages={'required': 'Blood type is required.'})
