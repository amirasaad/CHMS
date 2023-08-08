from http import HTTPStatus
from uuid import uuid4

import requests


def post_to_create_customer(skip_assert=False):
    response = requests.post(
        "http://127.0.0.1:5000/customers",
        json={
            "first_name": "John",
            "last_name": "Smith",
            "email": f"{uuid4()}@example.com",
        },
    )
    if not skip_assert:
        assert response.status_code == HTTPStatus.CREATED
        assert "id" in response.json()
    return response.json()["id"]
