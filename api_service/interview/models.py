from django.db import models

import uuid

# Create your models here.


class Question(models.Model):
    text = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

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
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(default=uuid.uuid4(), null=False)

    class Meta:
        db_table = "answers"
