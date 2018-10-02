from rest_framework.exceptions import APIException


class InternalServerError(APIException):
    status_code = 500