import unittest
import json
from unit_test.login.login_inputs import *
HTTP_200_OK, HTTP_401_UNAUTHORIZED = 200, 401

tc = unittest.TestCase


def test_login_passed(client):
    # Issue a POST request.
    response = client.post('/users/authenticate', data=json.dumps(valid_payload), content_type='json')
    return response


def test_login_failed(client):
    # Issue a POST request.
    response = client.post('/users/authenticate', data=json.dumps(invalid_payload), content_type='json')
    return response
