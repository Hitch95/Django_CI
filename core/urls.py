from django.urls import path
from core.views import hello_world
from . import views

urlpatterns = [
    path('', hello_world),
]