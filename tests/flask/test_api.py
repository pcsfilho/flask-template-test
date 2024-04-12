# Other modules
import pytest

# Local modules
from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_api_hello(app):
    with app.test_client() as client:
        response = client.get("/api/tests/hello")
        assert response.status_code == 200
        assert response.json["status"] == "success"
        assert response.json["message"] == "Hello World!!"


def test_api_success(app):
    with app.test_client() as client:
        response = client.get("/api/tests/success")
        assert response.status_code == 200
        assert response.json["status"] == "success"
        assert response.json["data"]["title"] == "riad-azz"
        assert response.json["data"]["content"] == "Successful API response"