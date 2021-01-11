# coverage run -m pytest            coverage report -m
# python -m pytest test/test_5_user.py
import json
import datetime

import jwt
import pytest

from __init__ import *
from urls import user_urls


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
def user_data():
    user_data = {
        "username": "TEST",
        "email": "TEST@mail.com",
        "password": "TEST"
    }
    return user_data


#######################################################################################################################

def test_create_user_200(user_data):
    client = app.test_client()
    url = '/user'
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201


def test_create_user_nodata():
    client = app.test_client()
    url = '/user'
    response = client.post(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


@pytest.fixture()
def user_inv_data():
    user_inv_data = {
        "username": 1,
        "email": 1,
        "password": 1
    }
    return user_inv_data


def test_create_user_invinput(user_inv_data):
    client = app.test_client()
    url = '/user'
    response = client.post(url, data=json.dumps(user_inv_data), content_type='application/json')
    assert response.status_code == 400


def test_create_user_usrnmused(user_data):
    client = app.test_client()
    url = '/user'
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 409


#######################################################################################################################

def test_get_users():
    client = app.test_client()
    url = '/user'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


#######################################################################################################################

def test_user_by_id_200():
    client = app.test_client()
    url = '/user/1'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


def test_user_by_id_invid():
    client = app.test_client()
    url = '/user/100'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 406


#######################################################################################################################

def test_update_user_200(user_data):
    user_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/user?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 200


def test_update_user_invtoken(user_data):
    user_data['username'] = 'NewName'
    client = app.test_client()

    url = '/user?access_token=' + user_data['username']

    response = client.put(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 401


def test_update_user_notuser(user_data):
    user_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/user?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 403


def test_update_user_invid(user_data):
    user_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(100, 0)
    url = '/user?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 406


def test_update_user_nodata():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/user?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


#######################################################################################################################

@pytest.fixture()
def create_user2(user_data):
    user_data['username'] = 'Testing'
    client = app.test_client()
    url = '/user'
    client.post(url, data=json.dumps(user_data), content_type='application/json')
    return user_data


def test_delete_user_invtoken(create_user2):
    client = app.test_client()

    url = '/user?access_token=123'

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 401


def test_delete_user_notuser():
    client = app.test_client()

    encoded_jwt = encode_auth_token(2, 1)
    url = '/user?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 403


def test_delete_user_invid():
    client = app.test_client()

    encoded_jwt = encode_auth_token(200, 0)
    url = '/user?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 406


def test_delete_user_200():
    client = app.test_client()

    encoded_jwt = encode_auth_token(2, 0)
    url = '/user?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 200
    # python -m pytest test/test_5_user.py
