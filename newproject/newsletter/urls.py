from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('new',views.new,name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]
