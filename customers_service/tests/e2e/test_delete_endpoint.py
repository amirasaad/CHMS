from http import HTTPStatus

import requests

from customers_crud.config import APP_HOST

from .utils import post_to_create_customer


def test_should_return_status_200_for_valid_request():
    customer_id = post_to_create_customer(skip_assert=True)
    response = requests.delete(
        f"http://{APP_HOST}/customers/{customer_id}",
    )
    assert response.status_code == HTTPStatus.ACCEPTED
    assert response.json()["message"] == "Customer Deleted."
