from urllib import response
from django.shortcuts import render
from rest_framework import  status, generics, permissions
from rest_framework.views import APIView , Response , status
from rest_framework.response import Response
from .models import Tweet,Reach , MyTweets
from .serializers import TweetSerializer,ReachSerializer,MyTweetsSerializer

"""
List all tweets
"""
class TweetList(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    


"""
create , update and delete tweets
"""
class TweetCreateUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'slug'
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""
1-) Get All Users who Liked the tweet and likes count
2-) create Like
3-) unlike
"""

class Likes(APIView):
        

    def get(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        likes = tweet.likes.all()
        serializer = TweetSerializer(likes, many=True)
        return Response(serializer.data , {'likes Count' : likes.count()})
    def post(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.likes.add(user)
        return Response(status=status.HTTP_200_OK,)
    def delete(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.likes.remove(user)
        return Response(status=status.HTTP_200_OK)

class Comment(APIView):
    def get(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        comments = tweet.comments.all()
        serializer = TweetSerializer(comments, many=True)
        return Response(serializer.data , {'comments Count' : comments.count()})
    def post(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.comments.add(user)
        return Response(status=status.HTTP_200_OK,)
    def delete(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.comments.remove(user)
        return Response(status=status.HTTP_200_OK)

class shares(APIView):
    def get(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        shares = tweet.shares.all()
        serializer = TweetSerializer(shares, many=True)
        return Response(serializer.data , {'shares Count' : shares.count()})
    def post(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.shares.add(user)
        return Response(status=status.HTTP_200_OK,)
    def delete(self, request, slug, format=None):
        tweet = Tweet.objects.get(slug=slug)
        user = request.user
        tweet.shares.remove(user)
        return Response(status=status.HTTP_200_OK)


""" List MyTweets ordered by latest """


class MyTweetsList(generics.ListAPIView):
    queryset = MyTweets.objects.all()
    serializer_class = MyTweetsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-created_at') 



class TrendySentencesList(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_top_repeated_sentences(self):
        # get all tweets
        tweets = Tweet.objects.all()
        # get all sentences in all tweets
        sentences = []
        for tweet in tweets:
            sentences.append(tweet.content)
        # get all unique sentences
        unique_sentences = set(sentences)
        # get all repeated sentences
        repeated_sentences = []
        for sentence in unique_sentences:
            if sentences.count(sentence) > 1:
                repeated_sentences.append(sentence)
        # get all repeated sentences with their count
        repeated_sentences_with_count = []
        for sentence in repeated_sentences:
            repeated_sentences_with_count.append([sentence, sentences.count(sentence)])
        # sort the repeated sentences with their count
        repeated_sentences_with_count.sort(key=lambda x: x[1], reverse=True)
        # return the top 10 repeated sentences
        trend_sentences = repeated_sentences_with_count[:10]
        return Response({'trend_sentences' : trend_sentences})
    
