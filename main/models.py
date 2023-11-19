from django.db import models
from mypage.models import Receiver, Profile
from rest_framework import serializers

# Create your models here.

class Message(models.Model):
    CATEGORY_CHOICES = [
        ('today', 'Today'),
        ('simple', 'Simple'),
        ('special', 'Special'),
        ('cute', 'Cute'),
    ]

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='today',
        verbose_name='카테고리'
    )
    
    #sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='보낸이')
    #receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE, related_name='received_messages', verbose_name='받는이')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return f'{self.category} - {self.content} ({self.created_at})'