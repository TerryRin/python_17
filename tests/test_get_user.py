import requests
from jsonschema import validate

from schemas import get_user, get_list_users


def test_get_list_users(url_api):
    page = 1
    per_page = 12
    response = requests.get(f'{url_api}/api/users', params={"page": page, "per_page": per_page})
    body = response.json()
    validate(body['data'], get_list_users)
    assert response.status_code == 200
    assert len(body['data']) <= per_page


def test_get_user(url_api):
    response = requests.get(f'{url_api}/api/users/3')
    body = response.json()
    validate(body['data'], get_user)
    assert response.status_code == 200
    assert len(body['data']['id']) == 3


def test_get_user_not_found(url_api):
    response = requests.get(f'{url_api}/api/users/unknown')
    assert response.status_code == 404
    assert response.json() == {}
