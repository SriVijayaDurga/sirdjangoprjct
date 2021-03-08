"""api_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from application_interface.configurations.configuration_router import configurations_reportconfig_router
from application_interface.gateway.gateway_router import gateway_router
from application_interface.gateway.selected_gateway_router import selected_gateway_router
from application_interface.configurations.configuration_input_router import configurations_input_router
from application_interface.home.home_router import home_overview_router, home_router, houlry_router
from application_interface.node.node_router import get_all_nodes_router, node_router, nodes_router
from application_interface.welder.welder_router import welder_router, welder_mapping_router, unmapping_router, delete_welder_router, delete_welder_mapping_router
from application_interface.user.user_router import single_user_router, user_router, login_router
from application_interface.ticket.ticket_router import ticket_router, selected_ticket_router, get_live_ticket_router, update_ticket_router
from application_interface.predictions.prediction_router import prediction_warranty_router, wirefeed_prediction_router, fault_router, predictions_fault_by_date_router
from application_interface.machine.machine_router import live_data_router, get_live_report_router, machine_router, selected_machine_router, machine_warranty_router
from application_interface.machine.machine_router import machine_wirefeed_router, update_selected_machine_config
from application_interface.report.report_router import daily_report_router, report_details_router, power_report_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/authenticate', login_router),
    path('gateways', gateway_router),
    path('gateways/<str:gateway_id>', selected_gateway_router),
    path('configurations/', configurations_input_router),
    path('configurations/report/', configurations_reportconfig_router),
    path('home/', home_overview_router),
    path('home/wirefeed', home_router),
    path('home/hourly', houlry_router),
    path('nodes/<int:gateway_id>', get_all_nodes_router),
    path('nodes/<nodeaddr>', node_router),
    path('nodes', nodes_router),
    path('welder/', welder_router),
    path('welder/mapping/', welder_mapping_router),
    path('welder/unmapped/', unmapping_router),
    path('welder/<int:welderid>', delete_welder_router),
    path('welder/mapping/<int:welderid>', delete_welder_mapping_router),
    path('users/<str:userid>', single_user_router),
    path('users/', user_router),
    path('tickets/', selected_ticket_router),
    path('tickets/<int:ticketid>', update_ticket_router),
    path('tickets/getticket', ticket_router),
    path('tickets/getliveticket', get_live_ticket_router),
    path('predictions/warranty', prediction_warranty_router),
    path('predictions/wirefeed', wirefeed_prediction_router),
    path('predictions/fault', fault_router),
    path('predictions/fault/<int:machineid>', predictions_fault_by_date_router),
    path('machines/get-live-data/<int:machineid>', live_data_router),
    path('machines/getlivereport', get_live_report_router),
    path('machines', machine_router),
    path('machines/<int:machineid>', selected_machine_router),
    path('machines/warranty/<int:machineid>', machine_warranty_router),
    path('machines/config/<int:machineid>', update_selected_machine_config),
    path('machines/wirefeed/<int:machineid>', machine_wirefeed_router),
    path('reports/<int:machineid>', daily_report_router),
    path("reports/", report_details_router),
    path("reports/poweranalysis", power_report_router)


]
