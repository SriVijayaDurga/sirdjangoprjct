from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.user_queries import *
from database.pg_query_search import *
from supports.response_module import *


def read_user(request, userid):
    payload = jwt_checker(request=request)
    if request.method == 'GET':
        if payload != 0:
            try:
                if payload['permission']['read']:
                    entity_id = payload['entity_id']
                    user_id = userid
                    user_details = django_parameterized_query_search_admin_role(dql_sql=get_Selected_User,
                                                                                dql_data=(entity_id, user_id))
                else:
                    return response_unauthorised()

                return response_success(data=user_details)

            except Exception as err:
                return response_exception(err)
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return response_invalid_token()
        else:
            return response_invalid_token()
    else:
        return response_request_wrong()