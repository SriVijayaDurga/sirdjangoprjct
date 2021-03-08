from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.ticket_queries import *
from database.pg_query_search import *
from supports.response_module import *


def get_selected_tickets(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                machineid = request.GET.get('machineid')
                severity = request.GET.get('severity')
                startdate = request.GET.get('startdate')
                enddate = request.GET.get('enddate')
                user_id = payload['userid']
                userid = repr(user_id)
                entity_id = payload['entity_id']
                data = django_query_search_all_any_role(sql=getTickets_query.format(machineid=machineid,
                                                                                    severity=severity,
                                                                                    entity_id=entity_id,
                                                                                    userid=userid,
                                                                                    startdate=startdate,
                                                                                    enddate=enddate))
                data_tuple1 = (int(machineid), int(severity), int(startdate), int(enddate), user_id)
                getticketsbyparams = django_parameterized_query_search_admin_role(dql_sql=getTicketsbyallparams_query,
                                                                                  dql_data=data_tuple1)
                response = {"status": data,
                            "severity": getticketsbyparams}

            else:
                return response_unauthorised()

            return response_success(data=response)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
