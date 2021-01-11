# coverage run -m pytest            coverage report -m
# python -m pytest test/test_7_login.py
import datetime
import json

import jwt
import pytest

from __init__ import *
from urls import basic_urls, user_urls, admin_urls

app.config['TESTING'] = True


@pytest.fixture()
def user_data():
    user_data = {
        "username": "test",
        "email": "test@mail.com",
        "password": "test",
    }
    return user_data


@pytest.fixture()
def login_user():
    login_user = {
        "username": "test",
        "password": "test",
        "admin": 0
    }
    return login_user


def test_create_user(user_data):
    client = app.test_client()
    url = '/user'
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201


def test_create_admin(user_data):
    client = app.test_client()
    url = '/admin'
    response = client.post(url, data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201


#######################################################################################################################

def test_login_nodata():
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400


def test_login_invdata(login_user):
    login_user["admin"] = "@"
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 403


#######################################################################################################################

def test_login_user_200(login_user):
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 200


def test_login_user_invname(login_user):
    login_user["username"] = 'incorrect'
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 404


def test_login_user_invpassw(login_user):
    login_user["password"] = "incorrect"
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 403


#######################################################################################################################

def test_login_admin_200(login_user):
    login_user["admin"] = 1
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 200


def test_login_admin_invname(login_user):
    login_user["admin"] = 1
    login_user["username"] = 'incorrect'
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 404


def test_login_admin_invpassw(login_user):
    login_user["admin"] = 1
    login_user["password"] = "incorrect"
    client = app.test_client()
    url = '/login'
    response = client.put(url, data=json.dumps(login_user), content_type='application/json')
    assert response.status_code == 403


#######################################################################################################################
def encode_auth_token(id, admin):
    keys = {
        'id': id,
        'admin': admin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'iat': datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(keys, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    return encoded_jwt


def test_logout_200():
    client = app.test_client()
    encoded_jwt = encode_auth_token(1, 0)
    url = '/logout?access_token=' + encoded_jwt
    response = client.put(url,  content_type='application/json')
    assert response.status_code == 200


def test_logout_invtoken():
    client = app.test_client()
    url = '/logout?access_token=123'
    response = client.put(url, content_type='application/json')
    assert response.status_code == 401
