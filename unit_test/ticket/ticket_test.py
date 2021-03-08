import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.ticket.ticket_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_ticket_added_passed(client):
    """Newticket gets added successfully"""
    # Issue a POST request.
    response = client.post('/tickets/', valid_payload, format='json')
    return response


def test_ticket_added_failed(client):
    """Newticket gets added successfully"""
    # Issue a POST request.
    response = client.post('/tickets/', invalid_payload, format='json')
    return response


def test_ticket_get_all_tickets_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/tickets/getticket?startdate=1612419870000&enddate=1612419870000', format='json')
    return response


def test_ticket_selected_ticket_get_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/tickets/?startdate=1612419870000&enddate=1612419870000&machineid=123456&severity=2',
                          format='json')
    return response


def test_ticket_get_live_ticket_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/tickets/getliveticket', format='json')
    return response


def test_ticket_update_passed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.put('/tickets/5', update_valid_payload, format="json")
    return response


def test_ticket_update_failed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.put('/tickets/5', update_invalid_payload, format="json")
    return response
