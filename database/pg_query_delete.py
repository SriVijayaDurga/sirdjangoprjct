"""
Created on Thu Aug  7 15:41:06 2020

@author: LIVNSENSE TECHNOLOGIES

@description:

Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
"""

from supports.response_module import *
from django.db import connection as conn


# Query function to delete if specific role comes as 1 or 2 other role discared
def query_delete_specific_role(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                try:
                    for each_sql in sql:
                        cursor.execute(each_sql)
                    conn.commit()
                    return conn, 0

                except Exception as err:
                    return 0, err

        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_parameterized_query_delete(delete_sql, delete_tuple):
    """

    :param role_id: role id of the user
    :param sql: query to be executed must be in array
    :return: connection status
    """
    #if role_id == 1:
    if conn:
        with conn.cursor() as cursor:
            try:
                # For parameterized query
                print(delete_sql % delete_tuple)
                cursor.execute(delete_sql % delete_tuple)
                conn.commit()
                return conn, 0

            except Exception as err:
                return 0, err
    else:
        return response_nodbconn()
    # else:
    #     return response_unauthorised()
# Query function
def django_parameterized_query_multiple_delete(delete_sql, delete_tuple):
    """

    :param role_id: role id of the user
    :param sql: query to be executed must be in array
    :return: connection status
    """
    #if role_id == 1:
    if conn:
        with conn.cursor() as cursor:
            try:
                # For parameterized query
                print(delete_sql , delete_tuple)
                cursor.execute(delete_sql , delete_tuple)
                conn.commit()
                return conn, 0

            except Exception as err:
                return 0, err
    else:
        return response_nodbconn()
    # else:
    #     return response_unauthorised()


# Query function
def django_parameterized_query_delete_no_role(delete_sql, delete_tuple):
    """

    :param delete_tuple:
    :param delete_sql:
    :param role_id: role id of the user
    :param sql: query to be executed must be in array
    :return: connection status
    """
    if conn:
        with conn.cursor() as cursor:
            try:
                # For parameterized query
                cursor.execute(delete_sql % delete_tuple)
                conn.commit()
                return conn, 0

            except Exception as err:
                return 0, err
    else:
        return response_nodbconn()
