
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prime, name='prime'),
]
