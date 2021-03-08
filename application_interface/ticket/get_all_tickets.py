from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.ticket_queries import *
from database.pg_query_search import *
from supports.response_module import *


def get_all_tickets(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                startdate = int(request.GET.get('startdate'))
                enddate = int(request.GET.get('enddate'))
                user_id = payload['userid']
                userid = repr(user_id)
                entity_id = payload['entity_id']
                data = django_query_search_all_any_role(sql=getAllTicketsCalculated_query.format(userid=userid,
                                                        startdate=startdate, enddate=enddate, entity_id=entity_id))
            else:
                return response_unauthorised()

            return response_success(data=data)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
