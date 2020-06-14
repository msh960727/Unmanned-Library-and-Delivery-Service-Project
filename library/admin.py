from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'stock', 'slug', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['stock', 'available']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
