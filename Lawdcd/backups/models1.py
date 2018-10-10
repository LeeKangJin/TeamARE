# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from Lawdcd.routers import testdb_router
class Lawdcd(models.Model):
    local_code = models.TextField(db_column='Local_code', blank=True, null=True)  # Field name made lowercase.
    deal_ymd = models.TextField(db_column='Deal_ymd', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.IntegerField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.address
    
    class Meta:
        app_label='Lawdcd'
        db_table = 'testdb'
        managed = True