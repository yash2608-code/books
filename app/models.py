from django.db import models

# Create your models here.


class Book(models.Model):
    bookn = models.CharField(max_length=50, default="Book Name")
    authorn = models.CharField(max_length=50, default="Author Name")
    bookp = models.IntegerField(default=123)
    book_file = models.FileField(upload_to="books/", default="none.pdf")
