from django.contrib import admin
from .models import ArriveBook


class ArriveAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']


admin.site.register(ArriveBook, ArriveAdmin)
from django.contrib import admin

# Register your models here.
