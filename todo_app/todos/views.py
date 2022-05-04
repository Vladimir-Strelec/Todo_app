from rest_framework import views, generics
from rest_framework.response import Response

from todo_app.todos.models import TodoModels, CategoryModels
from todo_app.todos.serializers import TodoSerializers, CategorySerializers


class CategoryCreateListGenerics(generics.ListCreateAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers


class TodoCreateListGenerics(generics.ListCreateAPIView):
    queryset = TodoModels.objects.all()
    serializer_class = TodoSerializers
