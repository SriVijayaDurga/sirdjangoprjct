from supports.response_module import *
from django.db import connection as conn


# function to Return all rows from a cursor as a dict
def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    final_data = [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]
    if len(final_data) is 0:
        return None
    else:
        return final_data[0]


# Function to get the data from table without any role
def django_parameterized_query_search_no_role(dql_sql, dql_data):
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(dql_sql, dql_data)
            data = dictfetchall(cursor)
            return data
    else:
        return response_nodbconn()

def django_parameterized_query_search_raw(dql_sql, dql_data):
    """ Function to get the data from table without any role"""

    if conn:
        with conn.cursor() as cursor:
            cursor.execute(dql_sql, dql_data)
            data = cursor.fetchall()
            return data
    else:
        return response_nodbconn()


# Function to get the data from table without admin(1) role
def django_parameterized_query_search_admin_role(dql_sql, dql_data):
    if conn:
        with conn.cursor() as cursor:

            cursor.execute(dql_sql, dql_data)
            data = dictfetchall(cursor)
            return data
    else:
        return response_nodbconn()

# Function to get the data from table without admin(1) role
def django_parameterized_query_search_one_admin_role(dql_sql, dql_data):
    #if role_id == 1:
    if conn:
        with conn.cursor() as cursor:
            print(dql_sql % dql_data)
            cursor.execute(dql_sql % dql_data)
            data = dictfetchall(cursor)
            return data
        # else:
        #     return response_nodbconn()


# Query function with any role
def django_query_search_all_any_role(sql):
    #if role_id == 1:
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = dictfetchall(cursor)
            return data
    else:
        return response_nodbconn()
    # else:
    #     return response_unauthorised()


# Query function with any role return one
def django_query_search_one_any_role(role_id, sql):
    if role_id:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_search_one_auth(role_id, sql):
    if role_id == 1 or role_id == 2:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function
def django_query_search_many_auth(role_id, sql):
    if role_id == 1 or role_id == 2:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchall(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with any role
def django_query_search_all_super_admin_role(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchall(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with any role
def django_query_search_one_super_admin_role(role_id, sql):
    if role_id == 1:
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = dictfetchone(cursor)
                return data
        else:
            return response_nodbconn()
    else:
        return response_unauthorised()


# Query function with no role
def django_query_search_no_role_one(sql):
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = dictfetchone(cursor)
            return data
    else:
        return response_nodbconn()
