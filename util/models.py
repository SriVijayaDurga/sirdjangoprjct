# from django.db import models
#
#
# class Users(models.Model):
#     """Custom user model that supports using email instead of username"""
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     age = models.IntegerField()
#     city = models.CharField(max_length=200)
#     contact_number = models.IntegerField()
#     country = models.CharField(max_length=200)
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     gender = models.CharField(max_length=10)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=500)
#     pincode =models.IntegerField()
#     role = models.IntegerField()
#     state = models.CharField(max_length=200)
#     entity_id = models.IntegerField()
#     userid = models.CharField(max_length=200)
#     status = models.BooleanField(default=True)
#     #is_superuser = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = "users"
#
#
# class Rolemaster(models.Model):
#     """Custom user model that supports using email instead of username"""
#     id = models.AutoField(primary_key=True)
#
#     name = models.CharField(max_length=255, unique=True)
#     description = models.CharField(max_length=200)
#     role_code = models.CharField(max_length=200)
#     can_read = models.BooleanField(default=True)
#     can_create = models.BooleanField(default=True)
#     can_update = models.BooleanField(default=True)
#     can_delete = models.BooleanField(default=True)
#     can_download = models.BooleanField(default=True)
#     can_map = models.BooleanField(default=True)
#     can_view = models.BooleanField(default=True)
#     entity_id = models.IntegerField(unique=True)
#     status = models.BooleanField(default=True)
#     #is_superuser = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = "rolemaster"