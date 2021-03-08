from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.report_queries import *
from database.pg_query_search import *
from supports.response_module import *


def power_report(request):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            machineid = request.GET.get('machineid')
            startdate = int(request.GET.get('startdate'))
            enddate = int(request.GET.get('enddate'))
            converted_d1 = datetime.datetime.fromtimestamp(round(startdate / 1000))
            converted_d2 = datetime.datetime.fromtimestamp(round(enddate / 1000))
            d = converted_d2 - converted_d1
            days =d.days
            if payload['permission']['read'] == True and (days == 0 or days < 1):
                hourlypowerrecords = django_query_search_all_any_role(sql=hourlyPowerRecordPerMachine_query.
                                                                      format(machineid=machineid, startdate=startdate,
                                                                             enddate=enddate))
                if len(hourlypowerrecords) > 0:
                    sending_response = {
                            "daywise": hourlypowerrecords
                    }
                else:
                    sending_response = {
                                "daywise": []

                    }
                return response_success(sending_response)

            elif payload['permission']['read'] == True and days > 1:
                machineid = int(request.GET.get('machineid'))
                startdate = int(request.GET.get('startdate'))
                enddate = int(request.GET.get('enddate'))
                dailypowerrecordpermachine = django_query_search_all_any_role(sql=dailypowerrecordpermachine_query.
                                                                              format(machineid=machineid,
                                                                                     startdate=startdate,
                                                                                     enddate=enddate))
                if len(dailypowerrecordpermachine) > 0:
                    sending_response = {
                        "daywise": dailypowerrecordpermachine
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
