from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
    search_fields = ('sender__nickname', 'receiver__nickname', 'content')

admin.site.register(Message, MessageAdmin)
