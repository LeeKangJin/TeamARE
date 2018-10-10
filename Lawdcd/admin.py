# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Lawdcd.models import Lawdcd

# Register your models here.

class LawdcdAdmin(admin.ModelAdmin):
    list_display=('Local_code', 'Deal_ymd', 'Address', 'X', 'Y')
   

admin.site.register(Lawdcd, LawdcdAdmin)
