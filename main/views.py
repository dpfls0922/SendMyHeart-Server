from django.shortcuts import render
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mypage.models import Receiver, Profile
from .serializers import ReceiverSerializer
from rest_framework import serializers
from .models import Message
from django.shortcuts import get_object_or_404

#수신자 선택 뷰
@api_view(['GET'])
def choose_receiver(request):
    receivers = Receiver.objects.all()
    return render(request, 'select_receiver.html', {'receivers': receivers})

#오늘의 안부 리스트
@api_view(['GET'])
def today_messages(request):
    selected_receiver = request.GET.get('receiver', '')  # 선택한 수신자의 nickname 가져오기
    messages = Message.objects.all()
    return render(request, 'message_today.html', {'messages': messages, 'selected_receiver': selected_receiver})


#카테고리별 메시지 선택 뷰
def category_messages(request, category):
    messages = Message.objects.filter(category=category)
    return render(request, 'category_messages.html', {'category': category, 'messages': messages})


#메시지 선택 후 편집기 뷰
@api_view(['GET'])
def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'message_view.html', {'message': message})