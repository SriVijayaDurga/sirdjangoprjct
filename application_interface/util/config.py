import os
import yaml
from api_framework.jwt_creator import *
from api_framework.sql_queries.login_queries import *
from supports.response_module import *
from database.pg_query_search import *
#from util.query import USER_PERMISSIONS, USER_LOGIN
#from util.response_module import response_unauthorised
#from util.utility import django_parameterized_query_search_raw, jwt_creation, django_parameterized_query_search_no_role, \
 #   django_parameterized_format_query_search_no_role

def get_config(config_file):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, config_file)
    configs = None

    with open(abs_file_path, 'r') as config_file:
        try:
            configs = yaml.load_all(config_file, Loader=yaml.SafeLoader).__next__()
        except ValueError:
            raise
    return configs


class Config:
    test_settings = 'properties.yaml'
    test_configs = get_config(test_settings)

    def generate_test_token(self):
        username = 'vijaya123@gmail.com'
        # password = "admin@123"
        response = django_parameterized_query_search_no_role(
            dql_sql=USER_LOGIN, dql_data=(username, username,)

        )
        if not response:
            return response_unauthorised()
        login_userid = response[0]['id']
        response_2 = django_parameterized_query_search_raw(
            dql_sql=user_login_query, dql_data=(username,))
        response = jwt_creation(data=response_2[0][0],
                                userid=login_userid)
        return str(response['token'])


    def get_test_config(self):
        TOKEN = self.generate_test_token()
        # LICENSE_URL = self.test_configs['license_url']
        LOGIN_URL = self.test_configs['login_url']
        # USER_URL = self.test_configs['user_url']
        # OTP_URL = self.test_configs['otp_url']

        return TOKEN, LOGIN_URL
