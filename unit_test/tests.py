# from django.test import Client
from unit_test.login.login_test import *
from unit_test.user.user_test import *
from unit_test.configurations.configuration_test import *
from unit_test.gateway.gateway_test import *
from unit_test.home.home_test import *
from unit_test.node.node_test import *
from unit_test.report.report_test import *
from unit_test.predictions.prediction_test import *
from unit_test.ticket.ticket_test import *
from unit_test.welder.welder_test import *
from unit_test.machine.machine_test import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_409_FORBIDDEN = 200, 401, 403, 409
HTTP_404_NOT_FOUND = 404
tc = unittest.TestCase


class SimpleTest(tc):
    def setUp(self):
        # Every test needs a client.
        self.client = APIClient()
        self.client.defaults['HTTP_AUTHORIZATION'] = "Bearer " + TOKEN

    def successful_response(self, response):
        # Check that the response is OK.
        self.assertEqual(response.status_code, HTTP_200_OK)
        # Check if content data is available
        self.assertIsNotNone(response.content)

    def unauthorized(self, response):
        # Check that the response is unauthorized.
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
        # Check if content data is available
        self.assertIsNotNone(response.content)

    def failure_response(self, response):
        # Check that the response is unauthorized.
        self.assertEqual(response.status_code, HTTP_409_FORBIDDEN)
        # Check if content data is available
        self.assertIsNotNone(response.content)

    def failed_response(self, response):
        # Check that the response is unauthorized.
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
        # Check if content data is available
        self.assertIsNotNone(response.content)

# login
    def test_login_passed(self):
        response = test_login_passed(self.client)
        self.successful_response(response)

    def test_login_failed(self):
        response = test_login_failed(self.client)
        self.unauthorized(response)

# User_management
    def test_user_added_passed(self):
        response = test_user_added_passed(self.client)
        self.successful_response(response)

    def test_user_added_failed(self):
        response = test_user_added_failed(self.client)
        self.unauthorized(response)

    def test_user_get_passed(self):
        response = test_user_get_passed(self.client)
        self.successful_response(response)

    def test_all_users_get_passed(self):
        response = test_all_users_get_passed(self.client)
        self.successful_response(response)

    def test_user_delete_passed(self):
        response = test_user_delete_passed(self.client)
        self.successful_response(response)

    def test_user_update_passed(self):
        response = test_user_update_passed(self.client)
        self.successful_response(response)

    def test_user_update_failed(self):
        response = test_user_delete_failed(self.client)
        self.failed_response(response)

# configuration
    def test_confguration_added_passed(self):
        response = test_configuration_added_passed(self.client)
        self.successful_response(response)

    def test_configuration_added_failed(self):
        response = test_configuration_added_failed(self.client)
        self.unauthorized(response)

    def test_configuration_get_passed(self):
        response = test_configuration_get_passed(self.client)
        self.successful_response(response)

    def test_configuration_report_get_passed(self):
        response = test_configuration_report_get_passed(self.client)
        self.successful_response(response)

    def test_configuration_update_passed(self):
        response = test_configuration_update_passed(self.client)
        self.successful_response(response)

# Gateway
    def test_gateway_added_passed(self):
        response = test_gateway_added_passed(self.client)
        self.successful_response(response)

    def test_gateway_added_failed(self):
        response = test_gateway_added_failed(self.client)
        self.unauthorized(response)

    def test_gateway_get_passed(self):
        response = test_gateway_get_passed(self.client)
        self.successful_response(response)

    def test_selected_gateway_get_passed(self):
        response = test_selected_gateway_get_passed(self.client)
        self.successful_response(response)

    def test_gateway_delete_passed(self):
        response = test_gateway_delete_passed(self.client)
        self.successful_response(response)

    def test_gateway_delete_failed(self):
        response = test_gateway_delete_failed(self.client)
        self.failed_response(response)

    def test_gateway_update_passed(self):
        response = test_gateway_update_passed(self.client)
        self.successful_response(response)

    def test_gateway_update_failed(self):
        response = test_gateway_update_failed(self.client)
        self.unauthorized(response)

# Home
    def test_home_total_wirefeed_get_passed(self):
        response = test_home_total_wirefeed_get_passed(self.client)
        self.successful_response(response)

    def test_home_hourly_wirefeed_get_passed(self):
        response = test_home_hourly_wirefeed_get_passed(self.client)
        self.successful_response(response)

    def test_home_overview_get_passed(self):
        response = test_home_overview_get_passed(self.client)
        self.successful_response(response)

# Node
    def test_node_added_passed(self):
        response = test_node_added_passed(self.client)
        self.successful_response(response)

    def test_node_added_failed(self):
        response = test_node_added_failed(self.client)
        self.unauthorized(response)

    def test_node_get_all_passed(self):
        response = test_node_get_all_passed(self.client)
        self.successful_response(response)

    def test_node_get_selected_passed(self):
        response = test_node_get_selected_passed(self.client)
        self.successful_response(response)

    def test_node_delete_passed(self):
        response = test_node_delete_passed(self.client)
        self.successful_response(response)

    def test_node_delete_failed(self):
        response = test_node_delete_failed(self.client)
        self.failed_response(response)

    def test_node_update_passed(self):
        response = test_node_update_passed(self.client)
        self.successful_response(response)

    def test_node_update_failed(self):
        response = test_node_update_failed(self.client)
        self.unauthorized(response)

# Predictions
    def test_prediction_get_warranty_passed(self):
        response = test_prediction_get_warranty_passed(self.client)
        self.successful_response(response)

    def test_prediction_get_wirefeed_passed(self):
        response = test_prediction_get_wirefeed_passed(self.client)
        self.successful_response(response)

    def test_prediction_get_allfault_passed(self):
        response = test_prediction_get_allfault_passed(self.client)
        self.successful_response(response)

    def test_prediction_get_selected_fault_passed(self):
        response = test_prediction_get_selected_fault_passed(self.client)
        self.successful_response(response)

# Report
    def test_report_get_report_details_passed(self):
        response = test_report_get_report_details_passed(self.client)
        self.successful_response(response)

    def test_report_get_dailyreport_passed(self):
        response = test_report_get_dailyreport_passed(self.client)
        self.successful_response(response)

    def test_report_get_powerreport_passed(self):
        response = test_report_get_powerreport_passed(self.client)
        self.successful_response(response)
#
# Ticket

    def test_ticket_added_passed(self):
        response = test_ticket_added_passed(self.client)
        self.successful_response(response)

    def test_ticket_added_failed(self):
        response = test_ticket_added_failed(self.client)
        self.unauthorized(response)

    def test_ticket_get_all_tickets_passed(self):
        response = test_ticket_get_all_tickets_passed(self.client)
        self.successful_response(response)

    def test_ticket_selected_ticket_get_passed(self):
        response = test_ticket_selected_ticket_get_passed(self.client)
        self.successful_response(response)

    def test_ticket_get_live_ticket_passed(self):
        response = test_ticket_get_live_ticket_passed(self.client)
        self.successful_response(response)

    def test_ticket_update_passed(self):
        response = test_ticket_update_passed(self.client)
        self.successful_response(response)

    def test_ticket_update_failed(self):
        response = test_ticket_update_failed(self.client)
        self.unauthorized(response)

# Welder
    def test_welder_added_passed(self):
        response = test_welder_added_passed(self.client)
        self.successful_response(response)

    def test_welder_added_failed(self):
        response = test_welder_added_failed(self.client)
        self.unauthorized(response)

    def test_welder_mapping_added_passed(self):
        response = test_welder_mapping_added_passed(self.client)
        self.successful_response(response)

    def test_welder_get_welder_passed(self):
        response = test_welder_get_welder_passed(self.client)
        self.successful_response(response)

    def test_welder_get_welder_machine_mapping_passed(self):
        response = test_welder_get_welder_machine_mapping_passed(self.client)
        self.successful_response(response)

    def test_welder_get_welder_unmapping_passed(self):
        response = test_welder_get_welder_unmapping_passed(self.client)
        self.successful_response(response)

    def test_welder_update_passed(self):
        response = test_welder_update_passed(self.client)
        self.successful_response(response)

    def test_welder_update_failed(self):
        response = test_welder_update_failed(self.client)
        self.unauthorized(response)

    def test_welder_mapping_update_passed(self):
        response = test_welder_mapping_update_passed(self.client)
        self.successful_response(response)

    def test_welder_delete_passed(self):
        response = test_welder_delete_passed(self.client)
        self.successful_response(response)

    def test_welder_mapping_delete_passed(self):
        response = test_welder_mapping_delete_passed(self.client)
        self.successful_response(response)

# Machine
    def test_machine_added_passed(self):
        response = test_machine_added_passed(self.client)
        self.successful_response(response)

    def test_machine_added_failed(self):
        response = test_machine_added_failed(self.client)
        self.unauthorized(response)

    def test_machine_get_passed(self):
        response = test_machine_get_passed(self.client)
        self.successful_response(response)

    def test_machine_get_wirefeed_passed(self):
        response = test_machine_get_wirefeed_passed(self.client)
        self.successful_response(response)

    def test_machine_get_warranty_passed(self):
        response = test_machine_get_warranty_passed(self.client)
        self.successful_response(response)

    def test_machine_get_live_data_passed(self):
        response = test_machine_get_live_data_passed(self.client)
        self.successful_response(response)

    def test_machine_get_selected_machine_passed(self):
        response = test_machine_get_selected_machine_passed(self.client)
        self.successful_response(response)

    def test_machine_get_report_data_passed(self):
        response = test_machine_get_report_data_passed(self.client)
        self.successful_response(response)

    def test_machine_update_passed(self):
        response = test_machine_update_passed(self.client)
        self.successful_response(response)

    def test_machine_config_update_passed(self):
        response = test_machine_config_update_passed(self.client)
        self.successful_response(response)

    def test_machine_wirefeed_update_passed(self):
        response = test_machine_wirefeed_update_passed(self.client)
        self.successful_response(response)

    def test_machine_warranty_update_passed(self):
        response = test_machine_warranty_update_passed(self.client)
        self.successful_response(response)

    def test_machine_delete_passed(self):
        response = test_machine_delete_passed(self.client)
        self.successful_response(response)
