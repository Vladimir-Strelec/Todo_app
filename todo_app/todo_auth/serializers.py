from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

UserModel = get_user_model()


class RegisterSerializersCreateApiView(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'],)
        user.save()
        return user

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result
