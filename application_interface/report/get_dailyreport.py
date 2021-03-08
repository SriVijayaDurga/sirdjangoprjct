from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.report_queries import *
from database.pg_query_search import *
from supports.response_module import *


def get_daily_report(request, machineid):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['read']:
                # machineid = request.GET.get('machineid')
                startdate = int(request.GET.get('startdate'))
                enddate = int(request.GET.get('enddate'))
                jobs = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordssum_query,
                                                                    dql_data=(startdate, enddate, machineid))
                if len(jobs) == 0:
                    data1 = {
                        "sum": jobs
                    }
                else:
                    data1 = jobs[0]['json_build_object']
                record_produced = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordsProduced_query,
                                                                                dql_data=(startdate, enddate, machineid))
                data3 = record_produced[0]['json_build_object']
                if data3['jobs'] == None:
                    data3['jobs'] = []
                getDailyRecordsPerMachines = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordsPerMachines_query,
                                                                               dql_data=(startdate, enddate, machineid))
                data2 = getDailyRecordsPerMachines[0]['json_build_object']
                if (data2['daywise'] == None):
                    data2['daywise'] =[]
                merge = {**data3, **data2, **data1}
                return response_success(data=merge)

            else:
                machineid = int(request.GET.get('machineid'))
                startdate = int(request.GET.get('startdate'))
                enddate = int(request.GET.get('enddate'))
                dailyPowerRecordPerMachine = django_parameterized_query_search_admin_role(dql_sql=dailypowerrecordpermachine_query,
                                                                                          dql_data=(machineid, startdate,
                                                                                                    enddate))
                if len(dailyPowerRecordPerMachine) > 0:
                    sending_response = {**dailyPowerRecordPerMachine
                    }
                else:
                    sending_response = {
                        "daywise": []
                    }
            return response_success(data=sending_response)

        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
