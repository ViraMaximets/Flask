from marshmallow import Schema, fields


class AdminSchema(Schema):
    adminId = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()

class UserSchema(Schema):
    userId = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
