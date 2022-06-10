from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views import Login, Register, profileUpdateRetrieveView,FollowUsers,followersList

app_name = "users"
from django.contrib import admin
from django.urls import path
from tweets.models import Tweet
from tweets.views import TweetList
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", Login.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("register/", Register.as_view()),
    path("profile/", profileUpdateRetrieveView.as_view()),
    path("follow/<int:id>/", FollowUsers.as_view()),
    path("connections/", followersList.as_view()),
    path("tweet/<slug>/", TweetList.as_view()),

]