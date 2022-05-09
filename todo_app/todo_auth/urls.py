from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from todo_app.todo_auth.views import RegisterView, LoginView, LogOutView, AuthView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),

    path('user/', AuthView.as_view()),
)
