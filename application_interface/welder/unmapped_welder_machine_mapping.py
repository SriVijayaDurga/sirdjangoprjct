from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.welder_queries import *
from database.pg_query_search import *
from supports.response_module import *


def unmapped_weldermachineMapping(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                entity_id = payload['entity_id']
                get_unmapped_welder = django_parameterized_query_search_admin_role(dql_sql=getUnMappedWelder_query,
                                                                            dql_data=(entity_id, ))
                get_unmapped_machine = django_parameterized_query_search_admin_role(dql_sql=getUnMappedMachine_query,
                                                                            dql_data=(entity_id,))
                message = {"welder": get_unmapped_welder,
                           "machine": get_unmapped_machine}
            else:
                return response_unauthorised()

            return response_success(data=message)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
