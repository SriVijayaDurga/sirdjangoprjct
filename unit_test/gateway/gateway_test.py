import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.gateway.gateway_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_gateway_added_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.post('/gateways', valid_payload, format='json')
    return response


def test_gateway_added_failed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.post('/gateways', invalid_payload, format='json')
    return response


def test_gateway_get_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/gateways', format='json')
    return response


def test_selected_gateway_get_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/gateways/u102', format='json')
    return response


def test_gateway_delete_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.delete('/gateways/u105', format='json')
    return response


def test_gateway_delete_failed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.delete('/gatewaysu103/', format="json")
    return response


def test_gateway_update_passed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.put('/gateways/u111', update_valid_payload, format="json")
    return response


def test_gateway_update_failed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.put('/gateways/u111', update_invalid_payload, format="json")
    return response
