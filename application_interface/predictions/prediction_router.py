from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.predictions.get_warrantypredictions import get_warranty
from application_interface.predictions.get_wirefeed import get_wirefeed
from application_interface.predictions.get_all_fault import get_all_fault
from application_interface.predictions.get_fault_by_date import get_fault_by_date
from supports.response_module import *


@csrf_exempt
def prediction_warranty_router(request):

    if request.method == GET:
        return get_warranty(request)

    else:
        return response_request_wrong()

@csrf_exempt
def wirefeed_prediction_router(request):

    if request.method == GET:
        return get_wirefeed(request)
    else:
        return response_request_wrong()

@csrf_exempt
def fault_router(request):

    if request.method == GET:
        return get_all_fault(request)
    else:
        return response_request_wrong()


@csrf_exempt
def predictions_fault_by_date_router(request, machineid):

    if request.method == GET:
        return get_fault_by_date(request, machineid)
    else:
        return response_request_wrong()