from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.machine_queries import *
from database.pg_query_search import *
from supports.response_module import *


def machine_read(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                userid = payload['userid']
                entity_id = payload['entity_id']
                data = django_parameterized_query_search_admin_role(dql_sql=getAllMachines,
                                                                    dql_data=(userid, entity_id))
            else:
                return response_unauthorised()

            return response_success(data=data)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
