import json
from api_framework.constants import *
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.machine_queries import *
from database.pg_query_insert import *
from supports.response_module import *
from supports.time_converter import *


def machine_add(request):
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
                entity_id = payload['entity_id']
                request_body = json.loads(request.body)
                # Parameters for parameterized query
                insert_tuple = (request_body[REQ_MACHINEID],
                                str(request_body[REQ_MACHINE_BUYER_COMPANY]), str(request_body[REQ_MACHINE_CITY]),
                                str(request_body[REQ_MACHINE_COUNTRY]), request_body[REQ_MACHINE_LATITUDE],
                                str(request_body[REQ_MACHINE_LONGITUDE]), str(request_body[REQ_MACHINE_MODEL]),
                                request_body[REQ_MACHINE_PINCODE], str(request_body[REQ_MACHINE_SENSOR_NODEID]),
                                str(request_body[REQ_MACHINE_STATE]), str(request_body[REQ_MACHINE_USERID]),
                                str(request_body[REQ_MACHINE_TAG_NAME]), time_converter(),
                                request_body[REQ_MACHINE_SALEDATE], entity_id)
                data, err = django_parameterized_query_insert(insert_sql=machine_insert_query,
                                                              insert_tuple=insert_tuple)
                # Parameterized insert query
                try:
                    # sale_date = request_body[REQ_MACHINE_SALEDATE]
                    # print(float(sale_date))
                    sale_date = request_body[REQ_MACHINE_SALEDATE]
                    # 10 days
                    warranty_date = sale_date - 864000000

                    warranty_insert_tuple = (request_body[REQ_WARRANTY_MACHINEID], sale_date,
                                             warranty_date, entity_id)

                    data, err = django_parameterized_query_insert(insert_sql=insert_warrantydetails_query,
                                                                  insert_tuple=warranty_insert_tuple)
                    print(data)
                    insert_tuple1 = (request_body[REQ_JOB_MACHINEID], request_body[REQ_JOBID],
                                     request_body[REQ_JOB_OPVOLT], request_body[REQ_JOB_MINTHRESHOLD],
                                     request_body[REQ_JOB_MAXTHRESHOLD], request_body[REQ_JOB_MIN_CURRENT_TIME],
                                     request_body[REQ_JOB_MAX_CURRENT_TIME], request_body[REQ_JOB_MIN_GASFLOW],
                                     request_body[REQ_JOB_MAX_GASFLOW], request_body[REQ_JOB_MIN_WIREFEED],
                                     request_body[REQ_JOB_MAX_WIREFEED], request_body[REQ_JOB_MIN_VOLTAGE],
                                     request_body[REQ_JOB_MAX_VOLTAGE], request_body[REQ_JOB_CURRENT_MAX_RANGE],
                                     time_converter(), entity_id, request_body[REQ_JOB_LOAD],
                                     request_body[REQ_JOB_NOLOAD],
                                     request_body[REQ_WIRESIZE])

                    data, err = django_parameterized_query_insert(insert_sql=insert_MachineConfig_query,
                                                                  insert_tuple=insert_tuple1)

                    # If data is zero, error has occurred
                    if data == 0:
                        return response_conflict(kind='Insert', err=str(err))
                except Exception as err:
                    return response_exception(err)
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
