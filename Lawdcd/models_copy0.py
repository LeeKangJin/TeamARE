# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Lawdcd(models.Model):
    id = models.IntegerField()
    local_code = models.TextField()
    deal_ymd = models.TextField()
    address = models.TextField()
    price = models.IntegerField()
    floor = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Lawdcd'
