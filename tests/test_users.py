import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_valid_user():
    """Test 1: Verifies that a valid user receives a 200 status code"""
    response = requests.get(f"{BASE_URL}?username=admin&password=qwerty")
    assert response.status_code == 200

def test_invalid_user():
    """Test 2: Verifies that an invalid user receives a 401 status code"""
    response = requests.get(f"{BASE_URL}?username=admin&password=admin")
    assert response.status_code == 401
