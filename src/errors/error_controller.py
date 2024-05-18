from typing import Dict
from src.errors.http_bad_request_error import HttpBadRequestError
from src.errors.http_not_found_error import HttpNotFoundError
from src.errors.http_unauthorized_error import HttpUnauthorizedError


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (
        HttpBadRequestError,
        HttpNotFoundError,
        HttpUnauthorizedError
    )):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "error": error.name,
                    "message": error.message
                }]
            }
        }

    return {
            "status_code": 500,
            "body": {
                "errors": [{
                    "error": "Server Error",
                    "message": str(error)
                }]
            }
        }
