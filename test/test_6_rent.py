# coverage run -m pytest            coverage report -m
# python -m pytest test/test_z_rent.py
import json
import datetime

import jwt
import pytest

from __init__ import *
from urls import rent_urls


def encode_auth_token(id, admin):
    keys = {
        'id': id,
        'admin': admin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'iat': datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(keys, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    return encoded_jwt


app.config['TESTING'] = True


@pytest.fixture()
def rent_data():
    rent_data = {
        "car_id": "1",
        "startTime": "0000-00-00",
        "endTime": "0010-10-10"
    }
    return rent_data


def test_create_rent_200(rent_data):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    assert response.status_code == 201


def test_create_rent_invtoken(rent_data):
    client = app.test_client()
    url = '/rent?access_token=123'
    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    assert response.status_code == 401


def test_create_rent_notuser(rent_data):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/rent?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    assert response.status_code == 403


def test_create_rent_nodata():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


def test_create_rent_invdata(rent_data):
    rent_data['car_id'] = "a"
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    assert response.status_code == 403


def test_create_rent_invid(rent_data):
    rent_data['car_id'] = 100
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    assert response.status_code == 404

#######################################################################################################################

def test_get_rents_200():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


def test_get_rents_invtoken():
    client = app.test_client()
    url = '/rent?access_token=123'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 401


def test_get_rents_notuser():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/rent?access_token=' + encoded_jwt
    response = client.get(url, content_type='application/json')
    assert response.status_code == 403

#######################################################################################################################

@pytest.fixture()
def create_rent2(rent_data):
    rent_data['startTime'] = '1111-00-00'
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent?access_token=' + encoded_jwt

    response = client.post(url, data=json.dumps(rent_data), content_type='application/json')
    return rent_data

def test_delete_rent_invtoken(create_rent2):
    client = app.test_client()
    url = '/rent/2/?access_token=123'
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 401


def test_delete_rent_notuser():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/rent/2/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 403


def test_delete_rent_invid():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent/200/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 404


def test_delete_rent_200():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/rent/2/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 200



    # python -m pytest test/test_z_rent.py
