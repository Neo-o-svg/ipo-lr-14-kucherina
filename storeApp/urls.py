from django.urls import path
from storeApp import views
from . import views

app_name = 'storeApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
]
