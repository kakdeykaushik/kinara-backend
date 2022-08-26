from rest_framework.exceptions import APIException


def http_409_conflict(message="Conflict"):
    ex = APIException(code=409, detail=message)
    return ex

