# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from Lawdcd.models import Lawdcd
from pprint import pprint
from django.db import connections
# Create your tests here.



class LawdcdTestcase(TestCase):
    def test_generate(self):
        Lawdcd.objects.all()