from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class CategoryModels(models.Model):
    name = models.CharField(max_length=20, validators=(MinLengthValidator(2),),)
    description = models.CharField(max_length=20, validators=(MinLengthValidator(2),),)

    def __str__(self):
        return f"{self.name}"


class TodoModels(models.Model):
    name = models.CharField(max_length=20, validators=(MinLengthValidator(2),),)
    description = models.CharField(max_length=200, validators=(MinLengthValidator(2),),)
    category = models.ForeignKey(CategoryModels, on_delete=models.CASCADE,)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,)
