import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.welder_queries import *
from database.pg_query_insert import *
from supports.response_module import *


def welder_add(request):
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
                print("user_create")
                request_body = json.loads(request.body)
                entity_id = payload['entity_id']
                # Parameters for parameterized query
                insert_tuple = (str(request_body[REQ_WELDER_FIRSTNAME]),
                                str(request_body[REQ_WELDER_LASTNAME]), request_body[REQ_WELDER_AGE],
                                str(request_body[REQ_WELDER_PHONE]), str(request_body[REQ_WELDER_PROFICIENCY]),
                                request_body[REQ_WELDER_GENDER], entity_id)
                # Parameterized insert query
                data, err = django_parameterized_query_insert(insert_sql=welder_insert_query,
                                                              insert_tuple=insert_tuple)
                print(err)
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
