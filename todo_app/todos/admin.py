from django.contrib import admin

from todo_app.todos.models import CategoryModels, TodoModels


@admin.register(CategoryModels)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoModels)
class TodoAdmin(admin.ModelAdmin):
    pass
