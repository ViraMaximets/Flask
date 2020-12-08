from flask import jsonify, request
from marshmallow import EXCLUDE

from main import app
import schema
from models import *


@app.route('/papaya')
def la():
    return '<h1> papayas </h1>'


@app.route("/")
def index():
    return '<h1> This is home page </h1>'

    #try:
     #   adminId = int(adminId)
   # except ValueError:
    #    return jsonify({'message': "Invalid Id supplied"}, 400)



############################################# user

@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()

    usere = schema.UserSchema(partial=("userId", "username", "email", "password")).load(data, unknown=EXCLUDE)

    db.session.add(usere)
    db.session.commit()

    return jsonify({'message': "OK"}, 200)





