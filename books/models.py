from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    pages = models.IntegerField()
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
     
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
