from django.urls import path


from todo_app.todo_auth.views import RegisterView, LogOutView
from rest_framework.authtoken import views

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogOutView.as_view(), name='logout'),
)
