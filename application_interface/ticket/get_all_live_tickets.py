from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.ticket_queries import *
from database.pg_query_search import *
from supports.response_module import *


def get_all_live_tickets(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                user_id = payload['userid']
                userid = repr(user_id)
                entity_id = payload['entity_id']
                data = django_query_search_all_any_role(sql=getAllTicketwoDT_query.format(userid=userid,
                                                                                          entity_id=entity_id))
            else:
                return response_unauthorised()

            return response_success(data=data)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
