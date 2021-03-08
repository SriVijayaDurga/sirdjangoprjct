from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.configurations.get_report_config import get_report_config
from application_interface.configurations.update_report_config import update_reportconfig

from supports.response_module import *


@csrf_exempt
def configurations_reportconfig_router(request):

    if request.method == GET:
        return get_report_config(request)
    elif request.method == PUT:
        return update_reportconfig(request)
    else:
        return response_request_wrong()
