from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.gateway.update_gateway import update_gateway
from application_interface.gateway.delete_gateway import delete_gateway
from application_interface.gateway.get_selected_gateway import get_selected_gateway
from supports.response_module import *


@csrf_exempt
def selected_gateway_router(request, gateway_id):

    if request.method == GET:
        return get_selected_gateway(request, gateway_id)

    elif request.method == PUT:
        return update_gateway(request, gateway_id)

    elif request.method == DELETE:
        return delete_gateway(request, gateway_id)

    else:
        return response_request_wrong()
