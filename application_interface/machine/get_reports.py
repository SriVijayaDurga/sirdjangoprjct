from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.machine_queries import *
from database.pg_query_search import *
from supports.response_module import *


def get_live_report(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                machineid = request.GET.get('machineid')
                startdate = request.GET.get('startdate')
                enddate = request.GET.get('enddate')

                data = django_query_search_all_any_role(sql=dailyRecordsPerMachines_query.format(machineid=machineid,
                                                                                                 startdate=startdate,
                                                                                                 enddate=enddate))

                return response_success(data=data)
            else:
                return response_unauthorised()

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
