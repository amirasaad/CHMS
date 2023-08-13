from http import HTTPStatus

import pytest
import requests

from customers_crud.config import APP_HOST

from .utils import post_to_create_customer


def test_should_return_status_201_for_valid_request():
    post_to_create_customer()


@pytest.mark.parametrize(
    "data,validation",
    [
        ({"first_name": "John", "last_name": "Smith"}, "email is required."),
        ({"first_name": "John", "email": "doe@example.com"}, "last_name is required."),
        ({"last_name": "John", "email": "doe@example.com"}, "first_name is required."),
        (
            {"first_name": "John", "last_name": "Smith", "email": "test"},
            "Invalid email.",
        ),
    ],
)
def test_required_fields(data, validation):
    response = requests.post(f"http://{APP_HOST}/customers", json=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert validation in response.json()["errors"]
