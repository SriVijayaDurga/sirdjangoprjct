from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.report_queries import *
from database.pg_query_search import *
from supports.response_module import *
import datetime


def get_report_details(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            startdate = int(request.GET.get('startdate'))
            enddate = int(request.GET.get('enddate'))
            converted_d1 = datetime.datetime.fromtimestamp(round(startdate / 1000))
            converted_d2 = datetime.datetime.fromtimestamp(round(enddate / 1000))
            d = converted_d2 - converted_d1
            days = d.days
            if payload['permission']['read']:
                dailyrecordssumm = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordssumALL_query,
                                                                                dql_data=(int(startdate), int(enddate)))
                data1 = dailyrecordssumm[0]['json_build_object']
                if data1['sum'] == None:
                    data1 = []
                dailyrecords_produceall = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordsProducedALL_query,
                                                                                dql_data=(int(startdate), int(enddate)))
                data3 = dailyrecords_produceall[0]['json_build_object']
                if data3['jobs'] == None:
                    data3['jobs'] = []
                getDailyRecordsALL = django_parameterized_query_search_admin_role(dql_sql=getDailyRecordsALL_query,
                                                                                dql_data=(int(startdate), int(enddate)))
                data2 = getDailyRecordsALL[0]['json_build_object']


                if data2['daywise'] == None:
                    data2['daywise'] = []
                merge = {**data3, **data2, **data1 }
                return response_success(data=merge)

            elif payload['permission']['read'] and days > 1:
                machineid = int(request.GET.get('machineid'))
                startdate = int(request.GET.get('startdate'))
                enddate = int(request.GET.get('enddate'))
                dailyPowerRecordPerMachine = django_parameterized_query_search_admin_role(dql_sql=dailypowerrecordpermachine_query,
                                                                                          dql_data=(machineid, startdate, enddate))
                if len(dailyPowerRecordPerMachine) > 0:
                    sending_response = {
                        "daywise": dailyPowerRecordPerMachine
                    }
                else:
                    sending_response = {
                        "daywise": []
                    }
                return response_success(data=sending_response)
            else:
                return response_exception(err='Unauthorized')
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
