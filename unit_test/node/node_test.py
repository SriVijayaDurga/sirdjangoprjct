import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.node.node_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_node_added_passed(client):
    """NewNode gets added successfully"""
    # Issue a POST request.
    response = client.post('/nodes', valid_payload, format='json')
    return response


def test_node_added_failed(client):
    """NewNode gets added failed"""
    # Issue a POST request.
    response = client.post('/nodes', invalid_payload, format='json')
    return response


def test_node_get_all_passed(client):
    """Get all node data successfully"""
    # Issue a GET request.
    response = client.get('/nodes/u103', format='json')
    return response


def test_node_get_selected_passed(client):
    """Get selected node data successfully"""
    # Issue a GET request.
    response = client.get('/nodes/0x124b001be46400', format='json')
    return response


def test_node_delete_passed(client):
    """Node deleted successfully"""
    # Issue a DELETE request.
    response = client.delete('/nodes/0x124b001be8300', format='json')
    return response


def test_node_delete_failed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.delete('/nodes0x124b001be21029/', format="json")
    return response


def test_node_update_passed(client):
    """Node updated successful"""
    # Issue a PUT request.
    response = client.put('/nodes/0x124b001be46202', update_valid_payload, format="json")
    return response


def test_node_update_failed(client):
    """NOde update failed"""
    # Issue a PUT request.
    response = client.put('/nodes/0x124b001be46202', update_invalid_payload, format="json")
    return response
