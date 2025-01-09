# image_convert/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('convert/', image_convert_view, name='image_convert'),
]