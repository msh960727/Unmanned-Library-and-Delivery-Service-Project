from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [

    path('', views.book_list, name='book_list'),

    path('<int:id>/<str:slug>/', views.book_detail, name='book_detail'),

]
