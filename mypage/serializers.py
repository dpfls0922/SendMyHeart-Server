from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from account.models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ReceiverSerializer(ModelSerializer):
    class Meta:
        model = Receiver
        fields = '__all__'