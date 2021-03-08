from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.home_queries import *
from database.pg_query_search import *
from supports.response_module import *
from supports.time_converter import *


def get_home_overview(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                current_date = time_converter()
                overview = django_parameterized_query_search_admin_role(dql_sql=getOverview_query,
                                                                        dql_data=(current_date,))


                machine_status = django_parameterized_query_search_admin_role(dql_sql=getMachinesStatus_query,
                                                                              dql_data=())
                data = {
                    "overview": overview,
                    "status": machine_status
                }
            else:
                return response_unauthorised()

            return response_success(data=data)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
