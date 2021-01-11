import json
import datetime

import jwt
import pytest

from __init__ import *
from urls import admin_urls


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
def admin_data():
    admin_data = {
        "username": "TEST",
        "email": "TEST@mail.com",
        "password": "TEST"
    }
    return admin_data


#######################################################################################################################

def test_create_admin_200(admin_data):
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 201


def test_create_admin_nodata():
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


@pytest.fixture()
def admin_inv_data():
    user_inv_data = {
        "username": 1,
        "email": 1,
        "password": 1
    }
    return user_inv_data


def test_create_admin_invinput(admin_inv_data):
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps(admin_inv_data), content_type='application/json')
    assert response.status_code == 400


def test_create_admin_usrnmused(admin_data):
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 409


#######################################################################################################################

def test_get_admins():
    client = app.test_client()
    url = '/admin'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


#######################################################################################################################

def test_admin_by_id_200():
    client = app.test_client()
    url = '/admin/1'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 200


def test_admin_by_id_invid():
    client = app.test_client()
    url = '/admin/100'
    response = client.get(url, content_type='application/json')
    assert response.status_code == 406


#######################################################################################################################

def test_update_admin_200(admin_data):
    admin_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/admin?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 200


def test_update_admin_invtoken(admin_data):
    admin_data['username'] = 'NewName'
    client = app.test_client()

    url = '/admin?access_token=' + admin_data['username']

    response = client.put(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 401


def test_update_admin_notadmin(admin_data):
    admin_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 0)
    url = '/admin?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 403


def test_update_admin_invid(admin_data):
    admin_data['username'] = 'NewName'
    client = app.test_client()

    encoded_jwt = encode_auth_token(100, 1)
    url = '/admin?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps(admin_data), content_type='application/json')
    assert response.status_code == 406


def test_update_admin_nodata():
    client = app.test_client()

    encoded_jwt = encode_auth_token(1, 1)
    url = '/admin?access_token=' + encoded_jwt

    response = client.put(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


#######################################################################################################################

@pytest.fixture()
def create_admin2(admin_data):
    admin_data['username'] = 'Testing'
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps(admin_data), content_type='application/json')
    return admin_data


def test_delete_admin_invtoken(create_admin2):
    client = app.test_client()

    url = '/admin?access_token=123'

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 401


def test_delete_admin_notadmin():
    client = app.test_client()

    encoded_jwt = encode_auth_token(2, 0)
    url = '/admin?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 403


def test_delete_admin_invid():
    client = app.test_client()

    encoded_jwt = encode_auth_token(200, 1)
    url = '/admin?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 406


def test_delete_admin_200():
    client = app.test_client()

    encoded_jwt = encode_auth_token(2, 1)
    url = '/admin?access_token=' + encoded_jwt

    response = client.delete(url, content_type='application/json')
    assert response.status_code == 200
    # python -m pytest test/test_admin.py
