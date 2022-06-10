from dataclasses import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

from users.models import User,profile


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

        data["username"] = self.user.username
        data["email"] = self.user.email

        return data


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            name = validated_data["name"],
            username=validated_data["username"],
            phone=validated_data["phone"],
            gender=validated_data["gender"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user

class ProfileSerializer(ModelSerializer):
    class  Meta:
        model = profile
        fields = "__all__"