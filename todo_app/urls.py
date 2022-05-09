from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/todos/', include('todo_app.todos.urls')),
    path('api/auth/', include('todo_app.todo_auth.urls')),
    path('', include('social_django.urls', namespace='social')),
]
