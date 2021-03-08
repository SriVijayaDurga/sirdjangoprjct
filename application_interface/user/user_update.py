import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.user_queries import *
from database.pg_query_modify import *
from supports.response_module import *


def user_update(request, userid):
    """
    this function used for adding device into db
    :param request: request from url
    :return: device inserted successfully
    """
    # Token from the authorization headers
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['update']:
                # Request body from request
                request_body = json.loads(request.body)
                entity_id = payload['entity_id']
                # Parameters for parameterized query
                update_tuple = (str(request_body[REQ_USER_FIRST_NAME]), str(request_body[REQ_USER_LAST_NAME]),
                                request_body[REQ_USER_AGE], request_body[REQ_USER_GENDER],
                                str(request_body[REQ_USER_MAILID]), request_body[REQ_USER_CONTACT_NUMBER],
                                str(request_body[REQ_USER_CITY]), str(request_body[REQ_USER_COUNTRY]),
                                str(request_body[REQ_USER_STATE]), str(request_body[REQ_USER_PINCODE]),
                                request_body[REQ_USER_ROLE], request_body[REQ_USER_STATUS],
                                userid, entity_id)
                # Parameterized update query
                data, err = django_parameterized_query_update(update_sql=user_update_query,
                                                              update_tuple=update_tuple)
                # If data is zero, error has occurred
                if data == 0:
                    return response_conflict(kind='update', err=str(err))
                # On success query, success response
                return response_success(data={"message": "Updated Successfully"})
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
