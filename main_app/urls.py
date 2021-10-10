from django.urls import path
from . import views

"""
This is be all our URLs, let's start formulating what URLs I will need.
"""

# this like app.use() in express
urlpatterns = [
    # Home Page
    path('', views.Home.as_view(), name="home"),
    # About Page
    path('about/', views.About.as_view(), name="about"),
    # All Books Page
    path('books/', views.BookList.as_view(), name="books"),
    # One Book Page
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    # Add Book Page
    path('books/new/', views.BookCreate.as_view(), name="book_create"),
    # Delete Book Confirmation Page
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name="book_delete"),
    # Update Book Info Page
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name="book_update"),
    # Search Results Page
    path ('search/', views.BookSearch.as_view(), name="book_search"),
    # All Subject Based URLs
    path('subjects/<int:pk>', views.SubjectDetail.as_view(), name="subject_detail")
]