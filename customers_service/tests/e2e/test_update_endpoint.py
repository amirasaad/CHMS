from http import HTTPStatus
from uuid import uuid4

import requests

from customers_crud.config import APP_HOST

from .utils import post_to_create_customer


def test_should_return_status_200_for_valid_request():
    customer_id = post_to_create_customer(skip_assert=True)
    response = requests.put(
        f"http://{APP_HOST}/customers/{customer_id}",
        json={
            "first_name": "Test",
            "last_name": "Smith",
            "email": f"{uuid4()}@example.com",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()["message"] == "Customer Updated."


def test_partial_update_return_status_200_for_valid_request():
    customer_id = post_to_create_customer(skip_assert=True)
    response = requests.put(
        f"http://{APP_HOST}/customers/{customer_id}",
        json={
            "first_name": "Test",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()["message"] == "Customer Updated."
