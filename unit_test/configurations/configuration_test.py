import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.configurations.configuration_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_configuration_added_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.post('/configurations/', valid_payload, format='json')
    return response


def test_configuration_added_failed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.post('/configurations/', invalid_payload, format='json')
    return response


def test_configuration_get_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/configurations/', format='json')
    return response


def test_configuration_report_get_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.get('/configurations/report/', format='json')
    return response


def test_configuration_update_passed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.put('/configurations/report/', update_valid_payload, format="json")
    return response
