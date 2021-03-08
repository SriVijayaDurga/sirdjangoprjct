import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.user_queries import *
from database.pg_query_insert import *
from supports.response_module import *


def user_add(request):
    """
    this function used for adding device into db
    :param request: request from url
    :return: device inserted successfully
    """
    # Token from the authorization headers
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['create']:
                # role_code = payload['userid']
                # Request body from request
                # entity_id = payload['entity_id']
                request_body = json.loads(request.body)

                # Parameters for parameterized query
                insert_tuple = (str(request_body[REQ_USERID]), request_body[REQ_USER_AGE],
                                str(request_body[REQ_USER_CITY]),
                                request_body[REQ_USER_CONTACT_NUMBER], str(request_body[REQ_USER_COUNTRY]),
                                str(request_body[REQ_USER_FIRST_NAME]), request_body[REQ_USER_GENDER],
                                str(request_body[REQ_USER_LAST_NAME]), str(request_body[REQ_USER_MAILID]),
                                str(request_body[REQ_USER_PASSWORD]), str(request_body[REQ_USER_PINCODE]),
                                request_body[REQ_USER_ROLE], str(request_body[REQ_USER_STATE]),
                                request_body[REQ_USER_STATUS], str(request_body[REQ_USER_USERNAME]),
                                request_body[REQ_USER_ENTITY_ID])
                # Parameterized insert query
                data, err = django_parameterized_query_insert(insert_sql=user_insert_query,
                                                              insert_tuple=insert_tuple)
                # If data is zero, error has occurred

                if data == 0:
                    return response_conflict(kind='Insert', err=str(err))
                # On success query, success response
                return response_success(data={"message": "Inserted Successfully"})
            else:
                return response_unauthorised()
        # If any kind of exception, response will be forbidden
        except Exception as err:
            return response_exception(err)
        # If JWT decode error or expiration, response will be unauthorized
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        # If wrong request, response will be unauthorized
        return response_invalid_token()
