from rest_framework.serializers import ModelSerializer
from .models import Tweet,Reach,MyTweets
class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"

class ReachSerializer(ModelSerializer):
    class Meta:
        model = Reach
        fields = "__all__"

class MyTweetsSerializer(ModelSerializer):
    class Meta:
        model = MyTweets
        fields = "__all__"