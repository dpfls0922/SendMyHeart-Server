from django.urls import path, include
from . import views

urlpatterns = [
    path('mypage/', include('mypage.urls')),
]