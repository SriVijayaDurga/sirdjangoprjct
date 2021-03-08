import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
# from unit_test.predictions.predictions_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_prediction_get_warranty_passed(client):
    """Get all prediction warranty data successfully"""
    # Issue a GET request.
    response = client.get('/predictions/warranty', format='json')
    return response


def test_prediction_get_wirefeed_passed(client):
    """Get wirefeed data successfully"""
    # Issue a GET request.
    response = client.get('/predictions/wirefeed', format='json')
    return response


def test_prediction_get_allfault_passed(client):
    """Get all fault data successfully"""
    # Issue a GET request.
    response = client.get('/predictions/fault', format='json')
    return response


def test_prediction_get_selected_fault_passed(client):
    """Get all fault data successfully"""
    # Issue a GET request.
    response = client.get('/predictions/fault/123456', format='json')
    return response

