from __future__ import unicode_literals

from django.db import models




class MultiDBRouter(object):  
    def db_for_read(self,model,**hints):
        if model._meta.app_label=='Lawdcd':
            return 'testdb'
        return 'default'
    
    def db_for_write(self,model,**hints):
        if model._meta.app_label=='Lawdcd':
            return 'testdb'
        return 'default'
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Lawdcd':
            return db=='testdb'
        return None
