from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.home.total_wirefeed_left import total_wirefeed_left
from application_interface.home.get_home_overview import get_home_overview
from application_interface.home.get_hourly import get_hourly
from supports.response_module import *


# Get_all_User_Details
@csrf_exempt
def home_router(request):

    if request.method == GET:
        return total_wirefeed_left(request)

    else:
        return response_request_wrong()


@csrf_exempt
def home_overview_router(request):
    if request.method == GET:
        return get_home_overview(request)
    else:
        return response_request_wrong()


@csrf_exempt
def houlry_router(request):
    if request.method == GET:
        return get_hourly(request)
    else:
        return response_request_wrong()
