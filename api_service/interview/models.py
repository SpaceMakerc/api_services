from django.db import models
from django.utils.timezone import now
import uuid

# Create your models here.


class Question(models.Model):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=now())

    def __str__(self):
        return self.pk

    class Meta:
        db_table = "questions"


class Answer(models.Model):
    question_id = models.ForeignKey(
        "Question",
        null=False,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(default=now())
    user_id = models.UUIDField(null=False)

    class Meta:
        db_table = "answers"
