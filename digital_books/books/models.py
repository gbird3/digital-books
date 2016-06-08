from django.db import models

# Define models here
class Category(models.Model):
    '''A list of the different book categories'''
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

class Book(models.Model):
    title = models.TextField(max_length=100)
    authorFirstName = models.TextField(max_length=50)
    category = models.ForeignKey(Category, related_name="categories")
    coverPicture = models.TextField(max_length=50)
    summary = models.TextField(max_length=150)
    pages = models.IntegerField(null=True, blank=True)


class Page(models.Model):
    book = models.ForeignKey(Book, related_name="books")
    fileName = models.TextField(max_length=100)
