from django.urls import path
from storeApp import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'storeApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
] 
