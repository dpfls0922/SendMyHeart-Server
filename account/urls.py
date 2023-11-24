from django.urls import path
from .views import SignupAPIView, AuthAPIView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('auth/', AuthAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)