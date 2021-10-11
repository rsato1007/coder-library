from django.urls import path
from . import views

"""
This is be all our URLs, let's start formulating what URLs I will need.
"""

# this like app.use() in express
urlpatterns = [
    # All Main Page URLs
    path('', views.Home.as_view(), name="home"),
    path ('search/', views.BookSearch.as_view(), name="book_search"),

    # All Book related pages
    path('about/', views.About.as_view(), name="about"),
    path('books/', views.BookList.as_view(), name="books"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    path('books/new/', views.BookCreate.as_view(), name="book_create"),
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name="book_delete"),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name="book_update"),

    # All Subject Based URLs
    path('subjects/<int:pk>', views.SubjectDetail.as_view(), name="subject_detail"),

    # All Author Based URLs
    path('author/', views.AuthorList.as_view(), name="authors"),
    path('author/new/', views.AuthorCreate.as_view(), name='author_create'),
]