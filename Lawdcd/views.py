# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Lawdcd.models import Lawdcd

def Listf(request): 
    lawdcd=Lawdcd.objects.all()
    context={'Lawdcd': lawdcd}
    
    return render(request, 'introduce/tables.html',context)

