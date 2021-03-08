from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.ticket.add_ticket import add_ticket
from application_interface.ticket.update_ticket import update_ticket_by_id
from application_interface.ticket.get_all_tickets import get_all_tickets
from application_interface.ticket.get_selected_tickets import get_selected_tickets
from application_interface.ticket.get_all_live_tickets import get_all_live_tickets
from supports.response_module import *


@csrf_exempt
def ticket_router(request):
    if request.method == GET:
        return get_all_tickets(request)

    else:
        return response_request_wrong()


@csrf_exempt
def update_ticket_router(request, ticketid):
    if request.method == PUT:
        return update_ticket_by_id(request, ticketid)

    else:
        return response_request_wrong()


@csrf_exempt
def selected_ticket_router(request):

    if request.method == GET:
        return get_selected_tickets(request)

    elif request.method == POST:
        return add_ticket(request)
    else:
        return response_request_wrong()


@csrf_exempt
def get_live_ticket_router(request):

    if request.method == GET:
        return get_all_live_tickets(request)
    else:
        return response_request_wrong()
