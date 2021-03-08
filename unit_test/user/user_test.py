import unittest
import json
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
from unit_test.user.user_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase


config = Config()
TOKEN = config.get_test_config()


def test_user_added_passed(client):
    """User gets added successfully"""
    # Issue a POST request.
    response = client.post('/users/', data=valid_payload, format='json')
    return response


def test_user_added_failed(client):
    """User gets added failed"""
    # Issue a POST request.
    response = client.post('/users/', ddata=json.dumps(invalid_payload), format='json')
    return response


def test_user_get_passed(client):
    """Get user data successfully"""
    # Issue a GET request.
    response = client.get('/users/admin', format='json')
    return response


def test_all_users_get_passed(client):
    """Get user data successfully"""
    # Issue a GET request.
    response = client.get('/users/', format='json')
    return response


def test_user_delete_passed(client):
    """User deleted successfully"""
    # Issue a DELETE request.
    response = client.delete('/users/admin1', format='json')
    return response


def test_user_delete_failed(client):
    """Deletion unsuccessful as no data provided"""
    # Issue a DELETE request.
    response = client.delete('/usersadmin/', format="json")
    return response


def test_user_update_passed(client):
    """User updated successful"""
    # Issue a PUT request.
    print("update")
    response = client.put('/users/admin11', update_valid_payload, format="json")
    return response


def test_user_update_failed(client):
    """User update failed"""
    # Issue a PUT request.
    response = client.put('/userss/admin11', update_valid_payload, format="json")
    return response
