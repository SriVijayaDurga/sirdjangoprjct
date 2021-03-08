import json
from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.configurations_queries import *
from database.pg_query_insert import *
from supports.response_module import *
from api_framework.constants import *


def add_newmachineinput(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['create']:
                # entity_id = payload['entity_id']
                request_body = json.loads(request.body)
                entity_id = payload['entity_id']
                # Parameters for parameterized query
                insert_tuple = (request_body[REQ_MACHINE_INPUT_ID], request_body[REQ_MACHINE_CYCLE_TIME],
                                request_body[REQ_MACHINE_PRODUCED], request_body[REQ_MACHINE_REJECTED],
                                request_body[REQ_MACHINE_TS], entity_id)
                # Parameterized insert query
                data, err = django_parameterized_query_insert(insert_sql=insert_MachineInput_query,
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
