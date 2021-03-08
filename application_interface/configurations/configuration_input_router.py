from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.configurations.add_machine_input import add_newmachineinput
from application_interface.configurations.get_machine_input import get_machine_input
from supports.response_module import *


@csrf_exempt
def configurations_input_router(request):

    if request.method == GET:
        return get_machine_input(request)

    elif request.method == POST:
        return add_newmachineinput(request)
    else:
        return response_request_wrong()
