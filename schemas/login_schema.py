from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    user_name = fields.Str(required=True, validate=validate.Length(min=0, max=100),error_message={"error_message": "User name is required."})
    password = fields.Str(required=True, validate=validate.Length(min=0, max=16), error_message={"error_message": "Password is required."})
