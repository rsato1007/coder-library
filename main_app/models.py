from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # We'll be using many to one here. (many books to one subject)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    image = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)