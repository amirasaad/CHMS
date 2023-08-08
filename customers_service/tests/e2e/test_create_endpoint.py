import requests
import pytest
from http import HTTPStatus
from uuid import uuid4

from .utils import post_to_create_customer



def test_should_return_status_201_for_valid_request():
    post_to_create_customer()


@pytest.mark.parametrize(
    "data,validation",
    [
        ({"first_name": "John", "last_name": "Smith"}, "Email is required."),
        ({"first_name": "John", "email": "doe@example.com"}, "LastName is required."),
        ({"last_name": "John", "email": "doe@example.com"}, "FirstName is required."),
    ],
)
def test_required_fields(data, validation):
    response = requests.post("http://127.0.0.1:5000/customers", json=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert validation in response.json()["errors"]
