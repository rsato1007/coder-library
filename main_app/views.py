from django.shortcuts import render, get_object_or_404
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = Subject.objects.all()
        context["books"] = Book.objects.all()[:4]
        return context

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

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'description', 'image', 'link', 'subject']
    template_name = "update_book.html"
    success_url = "/books/"

class BookSearch(ListView):
    template_name = "search_results.html"

    def get_queryset(self):
        title = self.request.GET.get('title')
        search_books = Book.objects.filter(title__icontains=title)
        return search_books

# All Subject Based Views
class SubjectDetail(ListView):
    template_name = "books_by_subject.html"

    def get_queryset(self):
        self.subject = Subject.objects.get(pk=self.kwargs.get('pk'))
        return Book.objects.filter(subject=self.subject)

# All Author based views
class AuthorList(TemplateView):
    template_name = "all_authors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context