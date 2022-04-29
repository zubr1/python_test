from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_given_no_input_when_calls_get_random_number_returns_http_200():
    response = client.get("/")
    assert response.status_code == 200
    
def test_given_wrong_input_when_calls_get_random_number_returns_http_422():
    response = client.get("/?range=test")
    assert response.status_code == 422
    
def test_given_incorrect_range_when_calls_get_random_number_returns_http_400():
    response = client.get("/?range=10-5")
    assert response.status_code == 400

#some deterministic test ;)
def test_given_correct_range_when_calls_get_random_number_returns_http_200_with_correct_result():
    response = client.get("/?range=200-200")
    assert response.status_code == 200
    assert response.json() == {'random_number': 200}
    