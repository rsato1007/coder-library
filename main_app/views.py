from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Subject

"""
This is where our functions go that do something when we get a URL request.
"""

# Create your views here.
class Temp(View):
    
    def get(self, requst):
        return HttpResponse("Page Under Construction")

class Home(CreateView):
    model = Subject
    fields = ['name']
    template_name = "home.html"
    success_url = ""