from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "hello world!!!"
    assert response.headers["content-type"].startswith("text/plain")


def test_only_one_route():
    assert len(app.routes) == 1
    assert client.get("/docs").status_code == 404
