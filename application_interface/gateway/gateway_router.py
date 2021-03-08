from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.gateway.add_gateway import add_new_gateway
from application_interface.gateway.get_all_gateways import get_all_gateways
from supports.response_module import *


@csrf_exempt
def gateway_router(request):

    if request.method == POST:
        return add_new_gateway(request)

    elif request.method == GET:
        return get_all_gateways(request)

    else:
        return response_request_wrong()
