from database.pg_query_search import *
from supports.response_module import *
import json
from api_framework.jwt_creator import *
from api_framework.sql_queries.login_queries import *
from api_framework.constants import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    try:
        request_body = json.loads(request.body)
        # Validation
        username = django_parameterized_query_search_no_role(dql_sql=check_username_exist_query,
                                                             dql_data=(request_body[REQ_USERNAME],))
        username_password = django_parameterized_query_search_no_role(dql_sql=username_password_validations,
                                                                      dql_data=(request_body[REQ_USERNAME],
                                                                                request_body[REQ_PASSWORD]))
        if len(username) > 0:
            if len(username_password) > 0:
                record = django_parameterized_query_search_no_role(dql_sql=user_login_query,
                                                                   dql_data=(request_body[REQ_USERNAME],
                                                                             request_body[REQ_PASSWORD]))

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
                    data = {
                        "userid": rec['userid'],
                        "role": rec['role'],
                        "status": rec['status']
                    }


                    merged = {**data, **jwt_creation(rec)}

                    return response_success(data=merged)

                else:
                    return response_unauthorised()
            else:
                return response_exception(err=WRONG_PASSWORD)
        else:
            return response_exception(err=USER_NOT_EXIST)

    except Exception as err:
        return response_exception(err)
