from django.urls import path

from todo_app.todos.views import TodoCreateListGenerics, CategoryCreateListGenerics

urlpatterns = [
    path('category/', CategoryCreateListGenerics.as_view(), name='category'),
    path('todo/', TodoCreateListGenerics.as_view(), name='todo'),
]