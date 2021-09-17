import os, pytest

from main import create_app

test_url = "/v1/tfidf?url=https://www.nytimes.com/2021/09/14/business/sale-surplus-federal-buildings.html&limit=3"


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_should_call_tfidf_endpoint_with_200(client):
    res = client.get(test_url)
    assert res is not None and res.status_code == 200


def test_should_call_tfidf_endpoint_with_404(client):
    res = client.get("/dummyurl")
    assert res is not None and res.status_code == 404


def test_should_call_tfidf_endpoint_with_405(client):
    res = client.post(test_url)
    assert res is not None and res.status_code == 405
