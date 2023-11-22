# your_app/serializers.py

from rest_framework import serializers
from mypage.models import Receiver, Profile
from .models import Message

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ('id', 'image', 'nickname')

# class MessageSerializer(serializers.ModelSerializer):
#     sender_nickname = serializers.SerializerMethodField()
#     receiver_nickname = serializers.SerializerMethodField()

#     class Meta:
#         model = 'main.Message'
#         fields = ('id', 'sender', 'receiver', 'content', 'created_at', 'sender_nickname', 'receiver_nickname')

    
#     def get_processed_content(self, obj):
#         # 원하는 처리를 수행
#         return obj.content.replace('{상대방}', '수신자 닉네임').replace('{본인}', '보낸이 닉네임')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'category', 'content', 'created_at', 'is_recommended']