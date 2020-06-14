from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    publisher = models.CharField(max_length=120)
    image_url = models.CharField(max_length=100000, blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    stock = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book_detail', args=[self.id, self.slug])
