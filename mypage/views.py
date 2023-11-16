import json
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def get_receivers(request):
    if request.method == 'GET':
        receiver = Receiver.objects.all().order_by('-id')
        serializer = ReceiverSerializer(receiver, many=True, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_receiver(request, receiver_id):
    if request.method == 'GET':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, context={'request': request})
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        receiver.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)