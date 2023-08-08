from flask import Flask, abort
from flask import request

app = Flask(__name__)


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
    return {}, 201
