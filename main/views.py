from django.shortcuts import render
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mypage.models import Receiver
from .serializers import ReceiverSerializer
from rest_framework import serializers
from .models import Message
from django.shortcuts import get_object_or_404
from .serializers import MessageSerializer

@api_view(['GET'])
def choose_receiver(request):
    receivers = Receiver.objects.all()
    serializer = ReceiverSerializer(receivers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def today_messages(request):
    selected_receiver = request.GET.get('receiver', '')
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response({'messages': serializer.data, 'selected_receiver': selected_receiver})

@api_view(['GET'])
def category_messages(request, category):
    messages = Message.objects.filter(category=category)
    serializer = MessageSerializer(messages, many=True)
    return Response({'category': category, 'messages': serializer.data})

@api_view(['GET'])
def view_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    serializer = MessageSerializer(message)
    return Response(serializer.data)
