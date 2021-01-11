from models import User, app, db
import pytest
from urls import basic_urls


def test_app():
    app.config['TESTING'] = True


@pytest.fixture()
def clear_db():
    db.drop_all()
    db.session.commit()
    db.create_all()


def test_db(clear_db):
    assert db.session.query(User).first() is None


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200





