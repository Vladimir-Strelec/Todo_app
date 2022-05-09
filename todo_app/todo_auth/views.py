from django.contrib.auth import get_user_model
from django.views import generic
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_app.todo_auth.serializers import RegisterSerializersCreateApiView, ViewsSerializer, LogoutSerializer

from rest_framework.authtoken import views

UserModel = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializersCreateApiView

    # def get(self, request):
    #     users = UserModel.objects.all()
    #     serializer = RegisterSerializersCreateApiView(users, many=True)
    #     return Response(data=serializer.data)


class LoginView(views.ObtainAuthToken):
    pass


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    @staticmethod
    def log_out(request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return request
        except:
            return request

    def initialize_request(self, *args, **kwargs):
        result = super().initialize_request(*args, **kwargs)
        self.log_out(result)
        return result



class TestView(views.APIView):

    def get(self, request):
        users = UserModel.objects.all()
        serializer = ViewsSerializer(users, many=True)
        return Response(serializer.data)


class AuthView(generic.TemplateView):
    template_name = 'social.html'
