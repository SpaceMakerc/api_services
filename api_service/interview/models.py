from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    ...


class Question(models.Model):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question_id = models.ForeignKey(
        "Question", null=False, on_delete=models.CASCADE
    )
    user_id = models.ForeignKey("CustomUser", null=False, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
