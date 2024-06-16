import requests


def test_delete_user(url_api):
    user_id = 5

    response = requests.delete(f'{url_api}/api/users/{user_id}')
    assert response.status_code == 204
    assert response.text == ''
