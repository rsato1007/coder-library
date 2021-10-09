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
    path('about/', views.Temp.as_view(), name="about"),
    # All Books Page
    path('books/', views.Temp.as_view(), name="books"),
    # One Book Page
    # Add Book Page
    # Delete Book Confirmation Page
    # Update Book Info Page
    # Search Results Page
]