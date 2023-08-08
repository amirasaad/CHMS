from http import HTTPStatus
from uuid import uuid4

import requests

from .utils import post_to_create_customer


def test_should_return_status_200_for_valid_request():
    customer_id = post_to_create_customer(skip_assert=True)
    response = requests.put(
        f"http://127.0.0.1:5000/customers/{customer_id}",
        json={
            "first_name": "Test",
            "last_name": "Smith",
            "email": f"{uuid4()}@example.com",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()["message"] == "Customer Updated."
