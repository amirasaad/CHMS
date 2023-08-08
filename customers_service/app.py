from http import HTTPStatus
from flask import Flask
from flask import request

from customers_crud import services
from customers_crud.repository import PureSQLRepository
from customers_crud.db import db_connection

app = Flask(__name__)

repo = PureSQLRepository(db_connection)


@app.route("/")
def health_check():
    return {"status": "running"}


@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.get_json()
    if "email" not in data:
        return {"errors": ["Email is required."]}, 400
    if "first_name" not in data:
        return {"errors": ["FirstName is required."]}, 400
    if "last_name" not in data:
        return {"errors": ["LastName is required."]}, 400
    customer_id = services.create_customer(
        data["first_name"], data["last_name"], data["email"], repo
    )
    if customer_id:
        return {"id": customer_id}, HTTPStatus.CREATED
    return {"message": "An error has been encountered."}, HTTPStatus.UNPROCESSABLE_ENTITY



@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json()
    if services.update_customer(
        customer_id, data["first_name"], data["last_name"], data["email"], repo
    ):
        return {"message": "Customer Updated."}, HTTPStatus.OK
    return {"message": "An error has been encountered."}, HTTPStatus.UNPROCESSABLE_ENTITY


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    if services.delete_customer(customer_id, repo):
        return {"message": "Customer Deleted."}, HTTPStatus.ACCEPTED
    return {"message": "An error has been encountered."}, HTTPStatus.UNPROCESSABLE_ENTITY



@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def get_customer(customer_id):
    customer = services.get_customer(customer_id, repo)
    if customer:
        return {customer.to_json()}, HTTPStatus.ACCEPTED
    return {"message": "An error has been encountered."}, HTTPStatus.UNPROCESSABLE_ENTITY
