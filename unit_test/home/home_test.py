import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
# from unit_test.home.home_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_home_total_wirefeed_get_passed(client):
    """get total wirefeed data successfully"""
    # Issue a GET request.
    response = client.get('/home/wirefeed', format='json')
    return response


def test_home_hourly_wirefeed_get_passed(client):
    """get home hourly data successfully"""
    # Issue a GET request.
    response = client.get('/home/hourly', format='json')
    return response


def test_home_overview_get_passed(client):
    """get home overview successfully"""
    # Issue a GET request.
    response = client.get('/home/', format='json')
    return response
