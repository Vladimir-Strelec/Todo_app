from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.response import Response

from todo_app.todos.models import TodoModels, CategoryModels

UserModel = get_user_model()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModels
        fields = "__all__"



class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoModels
        fields = ('name', 'description', 'category')



    def validate(self, attrs):
        attrs['user'] = self.initial_data['user']
        return attrs


    def create(self, validated_data):
        self.validate(attrs=validated_data)
        instance = TodoModels.objects.create(**validated_data)
        return instance
