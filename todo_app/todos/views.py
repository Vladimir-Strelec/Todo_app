from rest_framework import views, generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_app.todos.models import TodoModels, CategoryModels
from todo_app.todos.serializers import TodoSerializers, CategorySerializers


class CategoryCreateListGenerics(generics.ListCreateAPIView):
    queryset = CategoryModels.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class TodoCreateListGenerics(views.APIView, CreateModelMixin):
    serializer_class = TodoSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


    def get(self, request):
        todos = TodoModels.objects.all()
        serializer = self.serializer_class(todos, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        request.data._mutable = True
        request.data['user'] = request.user

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

