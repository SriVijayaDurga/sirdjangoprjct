import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.machine.machine_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_machine_added_passed(client):
    """New machine gets added successfully"""
    # Issue a POST request.
    response = client.post('/machines', valid_payload, format='json')
    return response


def test_machine_added_failed(client):
    """New machine gets added failed"""
    # Issue a POST request.
    response = client.post('/machines', invalid_payload, format='json')
    return response


def test_machine_get_passed(client):
    """Get machines data"""
    # Issue a GET request.
    response = client.get('/machines', format='json')
    return response


def test_machine_get_wirefeed_passed(client):
    """Get machine wirefeed data"""
    # Issue a GET request.
    response = client.get('/machines/wirefeed/331177', format='json')
    return response


def test_machine_get_warranty_passed(client):
    """Getting machine warranty details"""
    # Issue a GET request.
    response = client.get('/machines/warranty/221144', format='json')
    return response


def test_machine_get_live_data_passed(client):
    """Getting machine live data details"""
    # Issue a GET request.
    response = client.get('/machines/get-live-data/56324', format='json')
    return response


def test_machine_get_selected_machine_passed(client):
    """Getting selected machine details"""
    # Issue a GET request.
    response = client.get('/machines/10102', format='json')
    return response


def test_machine_get_report_data_passed(client):
    """Getting report data details"""
    # Issue a GET request.
    response = client.get('/machines/getlivereport?startdate=1613374247000&enddate=1613374247000&machineid=10102',
                          format='json')
    return response


def test_machine_update_passed(client):
    """Updated machine successfully"""
    # Issue a UPDATE request.
    response = client.put('/machines/101100', update_machine_valid_payload, format="json")
    return response


def test_machine_config_update_passed(client):
    """updated machine config successfululy"""
    # Issue a UPDATE request.
    response = client.put('/machines/config/331177', update_machineconfig_valid_payload, format="json")
    return response


def test_machine_wirefeed_update_passed(client):
    """updated machine wirefeed successfululy"""
    # Issue a UPDATE request.
    response = client.put('/machines/wirefeed/331177', update_wirefeed_valid_payload, format="json")
    return response


def test_machine_warranty_update_passed(client):
    """updated machine warranty successfululy"""
    # Issue a UPDATE request.
    response = client.put('/machines/warranty/101100', update_machine_warranty_valid_payload, format="json")
    return response


def test_machine_delete_passed(client):
    """machine deleted successfully"""
    # Issue a DELETE request.
    response = client.delete('/machines/4268', format='json')
    return response
