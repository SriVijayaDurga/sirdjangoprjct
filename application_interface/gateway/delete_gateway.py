from api_framework.jwt_checker import jwt_checker
from api_framework.jwt_creator import *
from api_framework.sql_queries.gateway_queries import *
from database.pg_query_delete import *
from supports.response_module import *


def delete_gateway(request, gateway_id):
    payload = jwt_checker(request=request)
    if payload != 0:
        try:
            if payload['permission']['delete']:
                entity_id = payload['entity_id']
                delete_tuple = (gateway_id, entity_id)
                data, err = django_parameterized_query_multiple_delete(delete_sql=deleteGateway_query,
                                                                       delete_tuple=delete_tuple)
                if data == 0:
                    return response_conflict(kind='Deleted', err=str(err))

                return response_success(data={"message": "Deleted Successfully"})
            else:
                return response_unauthorised()
        except Exception as err:
            return response_exception(err)
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return response_invalid_token()
    else:
        return response_invalid_token()
