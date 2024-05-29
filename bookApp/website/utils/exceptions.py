from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status

class customBadRequest(APIException):
  # status_code = status.HTTP_400_BAD_REQUEST
  default_detail = 'Bad Request.'
  default_code = 'bad_request'

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        # response.data['Error Type'] = "Bad Request"
    return response