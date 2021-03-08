import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.machine_queries import *
from database.pg_query_modify import *
from supports.response_module import *
from supports.time_converter import *


def machine_update(request, machineid):
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
                userid = payload['userid']
                # Request body from request
                request_body = json.loads(request.body)
                entity_id = payload['entity_id']
                # Parameters for parameterized query
                update_tuple = (str(request_body[REQ_MACHINE_BUYER_COMPANY]), str(request_body[REQ_MACHINE_CITY]),
                                str(request_body[REQ_MACHINE_COUNTRY]), request_body[REQ_MACHINE_DATE_OF_MANUFACTURE],
                                request_body[REQ_MACHINE_LATITUDE], request_body[REQ_MACHINE_LONGITUDE],
                                str(request_body[REQ_MACHINE_MODEL]), request_body[REQ_MACHINE_PINCODE],
                                time_converter(), request_body[REQ_MACHINE_SENSOR_NODEID],
                                str(request_body[REQ_MACHINE_STATE]), userid, machineid, entity_id)
                # Parameterized update query
                data, err = django_parameterized_query_update(update_sql=machine_update_query,
                                                              update_tuple=update_tuple)
                print(data)

                update_tuple = (request_body[REQ_JOB_MIN_GASFLOW], request_body[REQ_JOB_MAX_GASFLOW],
                                request_body[REQ_JOB_MIN_WIREFEED], request_body[REQ_JOB_MAX_WIREFEED],
                                request_body[REQ_JOB_MIN_VOLTAGE], request_body[REQ_JOB_MAX_VOLTAGE],
                                request_body[REQ_JOB_MINTHRESHOLD], request_body[REQ_JOB_MAXTHRESHOLD],
                                request_body[REQ_JOBCREATED], request_body[REQ_JOB_MIN_CURRENT_TIME],
                                request_body[REQ_JOB_MAX_CURRENT_TIME], request_body[REQ_JOBID],
                                request_body[REQ_JOB_CURRENT_MAX_RANGE], machineid, entity_id)

                data, err = django_parameterized_query_update(update_sql=updateMachineConfig_query,
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
