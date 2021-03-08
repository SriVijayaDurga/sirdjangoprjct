import unittest
# from django.test import Client
# from django.test import TestCase
# from rest_framework.test import APIClient
from unit_test.config import Config
# from unit_test.report.report_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_409_FORBIDDEN = 200, 401, 409
tc = unittest.TestCase
# import json


config = Config()
TOKEN = config.get_test_config()


def test_report_get_report_details_passed(client):
    """Get report details data successfully"""
    # Issue a GET request.
    response = client.get('/reports/?startdate=1612778164000&enddate=1613449663016&machineid=10102', format='json')
    return response


def test_report_get_dailyreport_passed(client):
    """Get daily report data successfully"""
    # Issue a GET request.
    response = client.get('/reports/123456?startdate=1612778164000&enddate=1612778164000', format='json')
    return response


def test_report_get_powerreport_passed(client):
    """Get all fault data successfully"""
    # Issue a GET request.
    response = client.get('/reports/poweranalysis?startdate=1613374247000&enddate=1613374247000&machineid=10102',
                          format='json')
    return response
