import pytest
from demo.app import create_app, User, db


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app()
    ctx = _app.test_request_context()
    ctx.push()

    _app.config["TESTING"] = True
    _app.testing = True

    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with _app.app_context():
        db.create_all()
        user1 = User(id=1, username="test user", email="some@email.co")
        db.session.add(user1)
        db.session.commit()

    yield _app
    ctx.pop()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client
