from django.contrib import admin

from todo_app.todo_auth.models import ShopUser


@admin.register(ShopUser)
class UserAdmins(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_superuser', 'is_staff')
