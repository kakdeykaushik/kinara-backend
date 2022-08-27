from rest_framework.exceptions import APIException
from rest_framework import status




class Unauthorized(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED



class Forbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN




class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND



class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT



class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR



