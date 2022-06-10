from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, ProfileSerializer, UserSerializer
from rest_framework import generics, permissions, status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .models import User , profile

"""
responsible for handling the login  of users
"""

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        except TokenError as e:
            raise InvalidToken(e.args[0])
        except Exception as e:
            print(e)
"""
responsible for handling the Registrations  of users

"""

class Register(generics.GenericAPIView):
    permission_class = permissions.AllowAny
    serializer_class = UserSerializer

    def post(self, request):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()
                return Response({"data": user_serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


"""
This view update and retrieve user profile
"""

class profileUpdateRetrieveView(generics.RetrieveUpdateAPIView):
    permission_class = (permissions.IsAuthenticated)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


"""
This view responsible for following and un following users
"""

class FollowUsers(APIView):
    permission_class = (permissions.IsAuthenticated)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data["user_id"])
            request.user.profile.following.add(user)
            return Response({"data": "followed"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data["user_id"])
            request.user.profile.following.remove(user)
            return Response({"data": "unfollowed"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

   
    
"""
this view is to list all the followers of the user and the Following list of the user , 
also it returns the count of the followers and following list of the user
"""

class followersList(APIView):
    queryset = profile.objects.all()
    permission_class = (permissions.IsAuthenticated)
    def get(self, request, *args, **kwargs):
        try:
            followers = request.user.profile.followers.all()
            following = request.user.profile.following.all()
            followersCount = followers.count()
            followingCount = following.count()
            return Response({"followers": followers, "following": following},{"followers count":followersCount, "following count": followingCount},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PasswordUpdate(APIView):
    permission_class = (permissions.IsAuthenticated)
    def post(self, request, *args, **kwargs):
        try:
            request.user.set_password(request.data["password"])
            request.user.save()
            return Response({"data": "password updated"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)