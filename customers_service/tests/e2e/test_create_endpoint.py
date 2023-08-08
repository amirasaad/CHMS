import requests
import pytest
from http import HTTPStatus


def test_should_return_status_201_for_valid_request():
    response = requests.post(
        "http://127.0.0.1:5000/customers",
        json={"first_name": "John", "last_name": "Smith", "email": "doe@example.com"},
    )
    assert response.status_code == HTTPStatus.CREATED


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
