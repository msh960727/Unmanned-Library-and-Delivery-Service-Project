from django.db import models
from library.models import Book
from orders.models import Order


class ArriveBook(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    stock = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
