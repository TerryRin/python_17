import requests
from jsonschema import validate

from schemas import put_user


def test_update_user(url_api, ):
    payload = {
        "name": "user3",
        "job": "user"
    }

    response = requests.put(f'{url_api}/api/users/3', json=payload)
    body = response.json()
    validate(body, put_user)

    assert response.status_code == 200
    assert response.json()['name'] == payload['name']  # Проверка имени
    assert response.json()['job'] == payload['job']  # Проверка должности
