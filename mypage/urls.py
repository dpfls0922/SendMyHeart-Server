from django.urls import path
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('receiver/all/', get_receivers, name='receivers_all'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)