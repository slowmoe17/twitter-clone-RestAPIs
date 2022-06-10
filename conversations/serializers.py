from rest_framework.serializers import ModelSerializer
from .models import conversation,message

class conversationSerializer(ModelSerializer):
    class Meta:
        model = conversation
        fields = "__all__"

class messageSerializer(ModelSerializer):
    class Meta:
        model = message
        fields = "__all__"