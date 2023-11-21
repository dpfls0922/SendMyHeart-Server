import json
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .models import *
from account.models import *
from .serializers import *

# 수정
@api_view(['GET', 'PUT'])
def my_profile_api(request, pk):
    if request.method == 'GET':
        User = get_user_model()
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        User = get_user_model()
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_receiver(request):
    if request.method == 'POST':
        serializer = ReceiverSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_receivers(request):
    if request.method == 'GET':
        receiver = Receiver.objects.all().order_by('-id')
        serializer = ReceiverSerializer(receiver, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def receiver_detail_api(request, receiver_id):
    if request.method == 'GET':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        receiver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)