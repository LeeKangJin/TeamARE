from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
import polls


class HomeView(view):
	def get(self,request, *args, **kwargs):
		return render(request, 'introduce/chart.html',{})

def get_data(request, *args, **kwargs):
	data = {
		"2008" : 100,
		"2009" : 110,
		"2010" : 120,
	}
	return JsonResponse(data)