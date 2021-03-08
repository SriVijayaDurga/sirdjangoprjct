from django.views.decorators.csrf import csrf_exempt
from api_framework.constants import *
from application_interface.node.add_node import add_newnode
from application_interface.node.update_node_byID import update_node
from application_interface.node.delete_node import node_delete
from application_interface.node.get_all_nodes import get_all_nodes
from application_interface.node.get_selected_node import get_selected_node
from supports.response_module import *


@csrf_exempt
def node_router(request, nodeaddr):

    if request.method == GET:
        return get_selected_node(request, nodeaddr)

    elif request.method == PUT:
        return update_node(request, nodeaddr)

    elif request.method == DELETE:
        return node_delete(request, nodeaddr)

    else:
        return response_request_wrong()

@csrf_exempt
def get_all_nodes_router(request, gateway_id):    # path('nodes/<gateway_id>', get_all_nodes_router)

    if request.method == GET:
        return get_all_nodes(request, gateway_id)

    else:
        return response_request_wrong()

@csrf_exempt
def nodes_router(request):

    if request.method == POST:
        return add_newnode(request)

    else:
        return response_request_wrong()