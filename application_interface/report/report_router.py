from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.report.get_dailyreport import get_daily_report
from application_interface.report.get_report_details import get_report_details
from application_interface.report.power_report import power_report
from supports.response_module import *


@csrf_exempt
def daily_report_router(request, machineid):

    if request.method == GET:
        return get_daily_report(request, machineid)

    else:
        return response_request_wrong()


@csrf_exempt
def report_details_router(request):

    if request.method == GET:
        return get_report_details(request)

    else:
        return response_request_wrong()


@csrf_exempt
def power_report_router(request):

    if request.method == GET:
        return power_report(request)

    else:
        return response_request_wrong()
