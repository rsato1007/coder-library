from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response

"""
This is where our functions go that do something when we get a URL request.
"""

# Create your views here.
class Temp(View):
    
    def get(self, requst):
        return HttpResponse("Page Under Construction")