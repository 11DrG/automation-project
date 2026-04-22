import requests

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres_c1da00091313414fb0d74df54836ddc0"
HEADERS = {"x-api-key": API_KEY}

def test_get_users():
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999", headers=HEADERS)
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "John", "job": "QA Engineer"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["name"] == "John"

def test_login_successful():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failed():
    payload = {"email": "invalid@reqres.in", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400