from marshmallow import Schema, fields


class UserSchema(Schema):
    userId = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Field(required=True)


class AdminSchema(Schema):
    adminId = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Field(required=True)


class BrandSchema(Schema):
    brandId = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CarSchema(Schema):
    carId = fields.Int(dump_only=True)
    brand_id = fields.Int(required=True)
    model = fields.Str(required=True)
    description = fields.Str()


class RentSchema(Schema):
    rentId = fields.Int(dump_only=True)
    owner_id = fields.Int(dump_only=True)
    car_id = fields.Int(required=True)
    startTime = fields.Str(required=True)
    endTime = fields.Str(required=True)

class LoginSchema(Schema):
    admin = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
