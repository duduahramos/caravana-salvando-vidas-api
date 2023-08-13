from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    email = fields.Str(required=True, validate=validate.Length(min=0, max=100),error_message={"error_message": "Email is required."})
    password = fields.Str(required=True, validate=validate.Length(min=0, max=16), error_message={"error_message": "Password is required."})
