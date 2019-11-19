# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SysRole(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysUser(models.Model):
    name = models.CharField(unique=True, max_length=50)
    auth_string = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "%s %s %s %s" % (self.name, self.auth_string, self.email, self.phone)

    @property
    def role(self):
        role_id = SysUserRole.objects.get(user_id=self.id).role_id
        return SysRole.objects.get(pk=role_id)

    class Meta:
        managed = False
        db_table = 'sys_user'



class SysUserRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sys_user_role'
