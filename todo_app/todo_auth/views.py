from django.contrib.auth import get_user_model
from rest_framework import views, generics
from rest_framework.authtoken.models import Token

from todo_app.todo_auth.serializers import RegisterSerializersCreateApiView

from rest_framework.authtoken import views

UserModel = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializersCreateApiView


# class LoginView(views.ObtainAuthToken):
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data,
    #                                        context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=user)
    #     from rest_framework.response import Response
    #     return Response({
    #         'token': token.key,
    #         'user_id': user.pk,
    #         'email': user.email
    #     })




class LogOutView(views.APIView):
    pass
