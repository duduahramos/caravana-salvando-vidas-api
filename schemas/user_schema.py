from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_message={"error_message2": "Name is required."})
    email = fields.Str(required=True, validate=validate.Length(min=0, max=100),error_message={"error_message": "Email is required."})
    password = fields.Str(required=True, validate=validate.Length(min=0, max=16), error_message={"error_message": "Password is required."})
