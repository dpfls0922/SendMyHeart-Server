from django.urls import path
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'mypage'

urlpatterns = [
    path('profile/<int:user_id>/', my_profile_api, name='my_profile'),
    path('receiver/create/<int:user_id>/', create_receiver, name='create_receivers'),
    path('receiver/all/<int:user_id>/', get_receivers, name='receivers_all'),
    path('receiver/<int:user_id>/<int:receiver_id>/', receiver_detail_api, name='receiver_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)