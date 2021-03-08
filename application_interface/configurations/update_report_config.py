import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.configurations_queries import *
from database.pg_query_modify import *
from supports.response_module import *


def update_reportconfig(request):
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
                update_tuple = (request_body[REQ_REPORTCONFIG_WELDER_DAILY_AVAILABLE],
                                request_body[REQ_REPORTCONFIG_WELDER_POWER_CONSUME],
                                request_body[REQ_REPORTCONFIG_POWER_RATE_UNIT],
                                request_body[REQ_REPORTCONFIG_IDLE_POWER_CONSUME],
                                request_body[REQ_REPORTCONFIG_DAILY_LABOUR_RATE],
                                request_body[REQ_REPORTCONFIG_DAILY_SHIFT_HOUR],
                                entity_id)
                # Parameterized update query
                data, err = django_parameterized_query_update(update_sql=updatereportConfig_query,
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
