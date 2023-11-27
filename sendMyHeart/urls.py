from django.contrib import admin
from django.urls import path, include
from account import urls as account_url
from main import urls as main_url
from mypage import urls as mypage_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(account_url)),
    path('main/', include(main_url)),
    path('mypage/', include(mypage_url)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)