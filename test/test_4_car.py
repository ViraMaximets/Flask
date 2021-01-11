# coverage run -m pytest            coverage report -m
# python -m pytest test/test_car.py
import json
import datetime

import jwt
import pytest

from __init__ import *
from urls import car_urls


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
def car_data():
    car_data = {
        "brand_id": "1",
        "model": "TEST",
        "description": "TEST"
    }
    return car_data


def test_create_car_200(car_data):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(car_data), content_type='application/json')
    assert response.status_code == 201


def test_create_car_invtoken(car_data):
    client = app.test_client()
    url = '/car?access_token=123'
    response = client.post(url, data=json.dumps(car_data), content_type='application/json')
    assert response.status_code == 401


def test_create_car_notadmin(car_data):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/car?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(car_data), content_type='application/json')
    assert response.status_code == 403


def test_create_car_nodata():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


def test_create_car_invdata(car_data):
    car_data['brand_id'] = "a"
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(car_data), content_type='application/json')
    assert response.status_code == 403


def test_create_car_invid(car_data):
    car_data['brand_id'] = 100
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car?access_token=' + encoded_jwt
    response = client.post(url, data=json.dumps(car_data), content_type='application/json')
    assert response.status_code == 403


#######################################################################################################################

def test_get_cars():
    client = app.test_client()
    url = '/car'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


#######################################################################################################################

def test_car_by_id_200():
    client = app.test_client()
    url = '/car/1/'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


def test_car_by_id_invid():
    client = app.test_client()
    url = '/car/100/'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 406


#######################################################################################################################

@pytest.fixture()
def car_update():
    car_update = {
        "description": "new description"
    }
    return car_update


def test_update_car_200(car_update):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car/1/?access_token=' + encoded_jwt
    response = client.put(url, data=json.dumps(car_update), content_type='application/json')
    assert response.status_code == 200


def test_update_car_invtoken(car_update):
    client = app.test_client()
    url = '/car/1/?access_token=123'
    response = client.put(url, data=json.dumps(car_update), content_type='application/json')
    assert response.status_code == 401


def test_update_car_notadmin(car_update):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/car/1/?access_token=' + encoded_jwt
    response = client.put(url, data=json.dumps(car_update), content_type='application/json')
    assert response.status_code == 403


def test_update_car_invid(car_update):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car/100/?access_token=' + encoded_jwt
    response = client.put(url, data=json.dumps(car_update), content_type='application/json')
    assert response.status_code == 406


def test_update_car_nodata():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car/1/?access_token=' + encoded_jwt
    response = client.put(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


#######################################################################################################################

@pytest.fixture()
def create_car2(car_data):
    car_data['model'] = 'Test2'
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car?access_token=' + encoded_jwt
    client.post(url, data=json.dumps(car_data), content_type='application/json')
    return car_data


def test_delete_car_notadmin(create_car2):
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/car/2/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 403


def test_delete_car_invid():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car/200/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 406


def test_delete_car_200():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/car/2/?access_token=' + encoded_jwt
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 200

    # python -m pytest test/test_4_car.py
