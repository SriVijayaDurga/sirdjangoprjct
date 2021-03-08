from database.pg_query_search import *
from api_framework.sql_queries.login_queries import *
from api_framework.constants import *
from api_framework.jwt_creator import *


class Config:
    #test_settings = 'properties.yaml'
    # test_configs = get_config(test_settings)

    def generate_test_token(self):
        username = 'admin'
        password = 'admin@123'
        response = django_parameterized_query_search_no_role(dql_sql=username_password_validations,
                                                                      dql_data=(username, password))
        # if not response:
        #     return response_unauthorised()
        username_password = django_parameterized_query_search_no_role(dql_sql=user_login_query,
                                                                      dql_data=(username, password))
        if len(username_password) > 0:
            record = django_parameterized_query_search_no_role(dql_sql=user_login_query,
                                                               dql_data=(username, password))
            if len(record) > 0:
                rec = {
                    "user_id": record[FIRST_ELEMENT]['user_id'],
                    "userid": record[FIRST_ELEMENT]['userid'],
                    "firstname": record[FIRST_ELEMENT]['firstname'],
                    "lastname": record[FIRST_ELEMENT]['lastname'],
                    "username": record[FIRST_ELEMENT]['username'],
                    "age": record[FIRST_ELEMENT]['age'],
                    "gender": record[FIRST_ELEMENT]['gender'],
                    "role": record[FIRST_ELEMENT]['role'],
                    "entity_id": record[FIRST_ELEMENT]['entity_id'],
                    "status": record[FIRST_ELEMENT]['status'],
                    "permission": {
                        "read": record[FIRST_ELEMENT]['can_read'],
                        "create": record[FIRST_ELEMENT]['can_create'],
                        "update": record[FIRST_ELEMENT]['can_update'],
                        "delete": record[FIRST_ELEMENT]['can_delete'],
                        "download": record[FIRST_ELEMENT]['can_download'],
                        "view": record[FIRST_ELEMENT]['can_view'],

                    }
                }
                response = jwt_creation(rec)
                token = str(response['token'])
                response2 = token[1:]
                # result = None
                result = response2.replace("'", "")

        return str(result)



    def get_test_config(self):
        TOKEN = self.generate_test_token()
        return TOKEN
