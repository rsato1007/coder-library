from django.db import models

# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#     link = models.CharField(max_length=100)
#     image = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subjects")

# class Subject(models.Model):
#     name = models.CharField(max_length=100)

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.CharField(max_length=500)
#     image = models.CharField(max_length=100)
#     books = models.ManyToManyField(Book)