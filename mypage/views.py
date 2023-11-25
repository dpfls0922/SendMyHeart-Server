import json
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import *
from account.models import *
from .serializers import *


@api_view(['GET', 'PUT'])
def my_profile_api(request, user_id):
    if request.method == 'GET':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_receiver(request, user_id):
    if request.method == 'POST':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        request.data['sender'] = user.pk
        
        serializer = ReceiverSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_receivers(request, user_id):
    if request.method == 'GET':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        receiver = Receiver.objects.filter(sender=user).order_by('-id')

        serializer = ReceiverSerializer(receiver, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def receiver_detail_api(request, user_id, receiver_id):
    if request.method == 'GET':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        receivers = Receiver.objects.filter(sender=user)
            
        receiver = get_object_or_404(receivers, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        receivers = Receiver.objects.filter(sender=user)
        
        receiver = get_object_or_404(receivers, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        receivers = Receiver.objects.filter(sender=user)
        
        receiver = get_object_or_404(receivers, pk=receiver_id)
        receiver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)