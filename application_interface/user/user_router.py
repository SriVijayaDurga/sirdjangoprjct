from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.user.read_all_users import user_all_read
from application_interface.user.user_update import user_update
from application_interface.user.user_delete import user_delete
from application_interface.user.user_add import user_add
#from unittest_users.views import user_add
from application_interface.user.read_user import read_user
from application_interface.login.authentication import login
#from login import views
from supports.response_module import *


@csrf_exempt
def user_router(request):

    if request.method == GET:
        return user_all_read(request)

    if request.method == POST:
        return user_add(request)


    else:
        return response_request_wrong()

@csrf_exempt
def single_user_router(request, userid):
    if request.method == GET:
        return read_user(request, userid)

    elif request.method == PUT:
        return user_update(request, userid)

    elif request.method == DELETE:
        return user_delete(request, userid)

    else:
        return response_request_wrong()

@csrf_exempt
def login_router(request):

    if request.method == POST:
        return login(request)
    else:
        return response_request_wrong()