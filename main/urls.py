from django.urls import path, include
from . import views
from .views import choose_receiver, today_messages, view_message, category_messages

app_name='main'

urlpatterns = [
    path('message/receiver/',choose_receiver, name="choose_receiver"),
    path('message/default', today_messages, name='today_messages'),
    path('message/view/<int:message_id>/', view_message, name='view_message'),
    path('message/<str:category>/', category_messages, name='category_messages'),
]