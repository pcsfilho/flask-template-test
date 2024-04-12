# Flask modules
from flask import Blueprint, request, abort
from werkzeug.exceptions import BadRequest, InternalServerError, Forbidden

# Local modules
from app.schemas.test import TestModel
from app.utils.api import success_response

tests_bp = Blueprint("tests", __name__, url_prefix="/tests")

@tests_bp.route("/hello", methods=["GET"])
def test_api_hello():
    return success_response(message="Hello World!!")


@tests_bp.route("/success", methods=["GET"])
def test_api_success():
    data = TestModel(title="riad-azz", content="Successful API response")
    data_dict = data.model_dump()
    return success_response(data_dict)