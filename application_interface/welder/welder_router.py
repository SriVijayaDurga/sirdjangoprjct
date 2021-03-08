from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.welder.welder_read import get_all_welders
from application_interface.welder.welder_add import welder_add
from application_interface.welder.welder_update import welder_update
from application_interface.welder.welder_delete import welder_delete
from supports.response_module import *
from application_interface.welder.get_welder_machine_mapping import welder_machine_mapping_read
from application_interface.welder.welder_mapping_add import welder_machine_mapping_add
from application_interface.welder.welder_mapping_update import welder_mapping_update
from application_interface.welder.unmapped_welder_machine_mapping import unmapped_weldermachineMapping
from application_interface.welder.delete_welder_machine_mapping import delete_weldermapping


@csrf_exempt
def welder_router(request):

    if request.method == GET:
        return get_all_welders(request)

    elif request.method == POST:
        return welder_add(request)

    elif request.method == PUT:
        return welder_update(request)

    else:
        return response_request_wrong()


@csrf_exempt
def delete_welder_router(request, welderid):

    if request.method == DELETE:
        return welder_delete(request, welderid)

    else:
        return response_request_wrong()


@csrf_exempt
def delete_welder_mapping_router(request, welderid):

    if request.method == DELETE:
        return delete_weldermapping(request, welderid)

    else:
        return response_request_wrong()


@csrf_exempt
def welder_mapping_router(request):

    if request.method == GET:
        return welder_machine_mapping_read(request)

    elif request.method == POST:
        return welder_machine_mapping_add(request)

    elif request.method == PUT:
        return welder_mapping_update(request)

    else:
        return response_request_wrong()


@csrf_exempt
def unmapping_router(request):

    if request.method == GET:
        return unmapped_weldermachineMapping(request)

    else:
        return response_request_wrong()
