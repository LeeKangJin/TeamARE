from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.introduce_index, name='introduce_index'),
	url(r'^login',views.introduce_login, name='introduce_login'),
	url(r'^register',views.introduce_register, name='introduce_register'),
	url(r'^tables',views.introduce_tables, name='introduce_tables'),
	url(r'^blank',views.introduce_blank, name='introduce_blank'),
	url(r'^charts',views.introduce_charts, name='introduce_charts'),
	url(r'^study',views.introduce_study, name='introduce_study'),
    url(r'^data',views.data, name='data'),
]