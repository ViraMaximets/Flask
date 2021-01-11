# coverage run -m pytest            coverage report -m
# python -m pytest test/test_3_brand.py
import json
import datetime

import jwt
import pytest

from __init__ import *
from urls import brand_urls


def encode_auth_token(id, admin):
    keys = {
        'id': id,
        'admin': admin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'iat': datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(keys, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    return encoded_jwt


@pytest.fixture()
def brand_data():
    brand_data = {
        "name": "TEST"
    }
    return brand_data


def test_create_brand_200(brand_data):
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand?access_token=' + encoded_jwt

    response = client.post(url, data=json.dumps(brand_data), content_type='application/json')
    assert response.status_code == 201


def test_create_brand_invtoken():
    client = app.test_client()

    url = '/brand?access_token=123'

    response = client.post(url, content_type='application/json')
    assert response.status_code == 401


def test_create_brand_notadmin():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/brand?access_token=' + encoded_jwt

    response = client.post(url, content_type='application/json')
    assert response.status_code == 403


def test_create_brand_nodata():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand?access_token=' + encoded_jwt

    response = client.post(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


@pytest.fixture()
def brand_invdata():
    brand_invdata = {
        "name": 123456
    }
    return brand_invdata


def test_create_brand_invdata(brand_invdata):
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand?access_token=' + encoded_jwt

    response = client.post(url, data=json.dumps(brand_invdata), content_type='application/json')
    assert response.status_code == 403

#######################################################################################################################

def test_get_brands():
    client = app.test_client()
    url = '/brand'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200

#######################################################################################################################

@pytest.fixture()
def create_brand2():
    brand_data = {
        "name": "TEST2"
    }
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand?access_token=' + encoded_jwt

    client.post(url, data=json.dumps(brand_data), content_type='application/json')
    return brand_data


def test_delete_brand_invtoken(create_brand2):
    client = app.test_client()
    url = '/brand/2?access_token=123'
    response = client.delete(url, content_type='application/json')
    assert response.status_code == 401


def test_delete_brand_notadmin():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/brand/2?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 403


def test_delete_brand_invid():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand/200?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 406


def test_delete_brand_200():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/brand/2?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 200

    # python -m pytest test/test_3_brand.py
