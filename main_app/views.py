from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Subject, Book, Author

"""
This is where our functions go that do something when we get a URL request.
"""

# Create your views here.
# This is where our main pages live
class Temp(View):
    
    def get(self, requst):
        return HttpResponse("Page Under Construction")

class Home(CreateView):
    model = Subject
    fields = ['name']
    template_name = "home.html"
    success_url = "/"

class About(TemplateView):
    template_name = "about.html"

# All Book Based Views
class BookList(TemplateView):
    template_name = "all_books.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'description', 'image', 'link', 'subject']
    template_name = "add_book.html"
    success_url = "/books/"

class BookDetail(DetailView):
    model = Book
    template_name = "one_book.html"

class BookDelete(DeleteView):
    model = Book
    template_name = "delete_book.html"
    success_url = "/books/"