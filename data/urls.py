from django.urls import path
from storeApp import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'data'

urlpatterns = [
    path('spec/', views.spec_list, name='spec_list'),
    path('spec/<str:id>/', views.spec_detail, name='spec_detail'),
    path('spec//', views.invalid_spec, name='invalid_spec'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
