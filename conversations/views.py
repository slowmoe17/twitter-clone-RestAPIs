from email.message import Message
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import message, conversation
from .serializers import messageSerializer, conversationSerializer

class conversationCreate(generics.CreateAPIView):
    queryset = conversation.objects.all()
    serializer_class = conversationSerializer
    permission_classes = (permissions.IsAuthenticated,)

class conversationList(generics.ListAPIView):
    serializer_class = conversationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return conversation.objects.filter(user=self.request.user)

class messageCreate(generics.CreateAPIView):
    queryset = message.objects.all()
    serializer_class = messageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
         serializer.save(sender=self.request.user)

class messageList(generics.ListAPIView):
    serializer_class = messageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return message.objects.filter(conversation=self.kwargs['pk'])
