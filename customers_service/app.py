from http import HTTPStatus

import mysql.connector
from flask import Flask, request

from customers_crud import services
from customers_crud.db import db_connection
from customers_crud.repository import MySQLRepository

app = Flask(__name__)

repo = MySQLRepository(db_connection)


@app.errorhandler(ValueError)
def handle_bad_request(e):
    return {"errors": [str(e)]}, HTTPStatus.BAD_REQUEST

@app.errorhandler(mysql.connector.errors.OperationalError)
def handle_db_error(e):
    return {"error": str(e)}, HTTPStatus.SERVICE_UNAVAILABLE

@app.route("/")
def health_check():
    return {"status": "running"}


@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.get_json()
    customer_id = services.create_customer(
        data.get("first_name", ""),
        data.get("last_name", ""),
        data.get("email", ""),
        repo,
    )
    if customer_id:
        return {"id": customer_id}, HTTPStatus.CREATED
    return {
        "message": "An error has been encountered."
    }, HTTPStatus.UNPROCESSABLE_ENTITY


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json()
    if services.update_customer(
        customer_id=customer_id,
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", ""),
        email=data.get("email", ""),
        repo=repo
    ):
        return {"message": "Customer Updated."}, HTTPStatus.OK
    return {
        "message": "An error has been encountered."
    }, HTTPStatus.UNPROCESSABLE_ENTITY


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    if services.delete_customer(customer_id, repo):
        return {"message": "Customer Deleted."}, HTTPStatus.ACCEPTED
    return {
        "message": "An error has been encountered."
    }, HTTPStatus.UNPROCESSABLE_ENTITY


@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = services.get_customer(customer_id, repo)
    if customer:
        return customer.to_json(), HTTPStatus.ACCEPTED
    return {
        "message": "An error has been encountered."
    }, HTTPStatus.UNPROCESSABLE_ENTITY
