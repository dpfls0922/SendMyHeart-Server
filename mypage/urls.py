from django.urls import path
from rest_framework.viewsets import ModelViewSet
from .views import *

urlpatterns = [
    path('receiver/all/', get_receivers, name='receivers_all'),
]