import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.welder.welder_input import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_welder_added_passed(client):
    """New welder gets added successfully"""
    # Issue a POST request.
    response = client.post('/welder/', valid_payload, format='json')
    return response


def test_welder_added_failed(client):
    """New welder gets added failed"""
    # Issue a POST request.
    response = client.post('/welder/', invalid_payload, format='json')
    return response


def test_welder_mapping_added_passed(client):
    """New welder mapping gets added successfully"""
    # Issue a POST request.
    response = client.post('/welder/mapping/', welder_mapping_add_valid_payload, format='json')
    return response


def test_welder_get_welder_passed(client):
    """Get welder data"""
    # Issue a GET request.
    response = client.get('/welder/', format='json')
    return response


def test_welder_get_welder_machine_mapping_passed(client):
    """Get welder machine mapping data"""
    # Issue a GET request.
    response = client.get('/welder/mapping/', format='json')
    return response


def test_welder_get_welder_unmapping_passed(client):
    """Getting welder unmapping details"""
    # Issue a GET request.
    response = client.get('/welder/unmapped/', format='json')
    return response


def test_welder_update_passed(client):
    """Updated welder successfully"""
    # Issue a UPDATE request.
    response = client.put('/welder/', update_welder_valid_payload, format="json")
    return response


def test_welder_update_failed(client):
    """Update welder failed"""
    # Issue a UPDATE request.
    response = client.put('/welder/', update_welder_invalid_payload, format="json")
    return response


def test_welder_mapping_update_passed(client):
    """updated welder mapping successfululy"""
    # Issue a UPDATE request.
    response = client.put('/welder/mapping/', update_welder_mapping_valid_payload, format="json")
    return response


def test_welder_delete_passed(client):
    """Welder deleted successfully"""
    # Issue a DELETE request.
    response = client.delete('/welder/7', format='json')
    return response


def test_welder_mapping_delete_passed(client):
    """Welder mapping deleted successfully"""
    # Issue a DELETE request.
    response = client.delete('/welder/mapping/3', format='json')
    return response
