import requests
from jsonschema import validate

from schemas import post_create_user


def test_create_user(url_api):
    payload = {
        "name": "Spock",
        "job": "Captain"
    }

    response = requests.post(f'{url_api}/api/users', json=payload)
    body = response.json()
    validate(body, post_create_user)

    assert response.status_code == 201
    assert response.json()['name'] == payload['name']  # Проверка имени
    assert response.json()['job'] == payload['job']  # Проверка должности
