from django.shortcuts import render, get_object_or_404
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
    
@api_view(['GET'])
def get_receiver(request, receiver_id):
    if request.method == 'GET':
        receiver = get_object_or_404(Receiver, pk=receiver_id)
        serializer = ReceiverSerializer(receiver, context={'request': request})
        return Response(serializer.data)
