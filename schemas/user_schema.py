from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=0, max=60), error_message={"error_message2": "Name is required."})
    user_name = fields.Str(required=True, validate=validate.Length(min=6, max=15),error_message={"error_message": "User name is required."})
    password = fields.Str(required=True, validate=validate.Length(min=0, max=15), error_message={"error_message": "Password is required."})
