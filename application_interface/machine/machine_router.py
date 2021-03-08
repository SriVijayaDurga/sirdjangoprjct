from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.machine.machine_get import machine_read
from application_interface.machine.get_selected_machine import get_selected_machine
from application_interface.machine.machine_add import machine_add
from application_interface.machine.machine_update import machine_update
from application_interface.machine.machine_delete import machine_delete
from supports.response_module import *
from application_interface.machine.upgrade_warranty_by_machineid import upgrade_warranty
from application_interface.machine.update_wirefeed_machine import update_wirefeed_by_machine
from application_interface.machine.get_wirefeed import get_wirefeed
from application_interface.machine.get_reports import get_live_report
from application_interface.machine.get_warranty_details import get_warranty
from application_interface.machine.update_machineconfig_by_id import update_machineconfig_by_id
from application_interface.machine.get_livedata import get_live_data


# Get_all_User_Details
@csrf_exempt
def live_data_router(request, machineid):

    if request.method == GET:
        return get_live_data(request, machineid)

    else:
        return response_request_wrong()


@csrf_exempt
def get_live_report_router(request):
    if request.method == GET:
        return get_live_report(request)
    else:
        return response_request_wrong()


@csrf_exempt
def machine_router(request):

    if request.method == GET:
        return machine_read(request)

    elif request.method == POST:
        return machine_add(request)
    else:
        return response_request_wrong()


@csrf_exempt
def selected_machine_router(request, machineid):

    if request.method == GET:
        return get_selected_machine(request, machineid)

    elif request.method == PUT:
        return machine_update(request, machineid)

    elif request.method == DELETE:
        return machine_delete(request, machineid)

    else:
        return response_request_wrong()


@csrf_exempt
def machine_warranty_router(request, machineid):
    if request.method == GET:
        return get_warranty(request, machineid)
    elif request.method == PUT:
        return upgrade_warranty(request, machineid)

    else:
        return response_request_wrong()


@csrf_exempt
def update_selected_machine_config(request, machineid):

    if request.method == PUT:
        return update_machineconfig_by_id(request, machineid)

    else:
        return response_request_wrong()


@csrf_exempt
def machine_wirefeed_router(request, machineid):

    if request.method == GET:
        return get_wirefeed(request, machineid)
    elif request.method == PUT:
        return update_wirefeed_by_machine(request, machineid)

    else:
        return response_request_wrong()
