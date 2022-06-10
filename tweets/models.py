from django.db import models
from django.forms import SlugField
from users.models import profile

from users.signals import User



class Tweet(models.Model):
    owner = models.ForeignKey(profile, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='tweet_images', blank=True, null=True)
    video = models.FileField(upload_to='tweet_videos', blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = SlugField(max_length=10)

    def __str__(self):
        return self.owner.user.username + " | " + self.content

    def get_absolute_url(self):
        return f"/tweet/{self.slug}/"

class Reach(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(profile, related_name='likes', blank=True)
    shares = models.ManyToManyField(profile, related_name='shares', blank=True)
    comments = models.ManyToManyField(profile, related_name='comments', blank=True)
    def __str__(self):
        return self.tweet.owner.user.username + " | " + self.user.user.username

class MyTweets(models.Model):
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_shared = models.BooleanField(default=False)

    def is_shared(self):
        if self.tweet.profile.user.username != self.user.user.username:
            return True
        else:
            return False
    
    def __str__(self):
        return f' : shared By {self.user.user.username} | Post Owner : {self.tweet.owner.user.username} | Post Content : {self.tweet.content}'