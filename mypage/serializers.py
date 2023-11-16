from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class ReceiverSerializer(ModelSerializer):
    class Meta:
        model = Receiver
        fields = '__all__'