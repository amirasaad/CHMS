from http import HTTPStatus

import requests

from customers_crud.config import APP_HOST

from .utils import post_to_create_customer


def test_should_return_status_200_for_valid_request():
    customer_id = post_to_create_customer(skip_assert=True)
    response = requests.get(
        f"http://{APP_HOST}/customers/{customer_id}",
    )
    assert response.status_code == HTTPStatus.ACCEPTED
    assert "id" in response.json()
    assert "first_name" in response.json()
    assert "last_name" in response.json()
    assert "email" in response.json()
