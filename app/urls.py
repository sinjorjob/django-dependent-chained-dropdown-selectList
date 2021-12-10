from django.urls import path
from .views import *

urlpatterns = [
    path('get-prefecture', getPrefecture, name='get-prefecture'),
    path('process-form', processForm, name='process-form'),
]
