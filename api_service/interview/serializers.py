from rest_framework import serializers

from interview.models import Question, Answer
from datetime import datetime


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "text", "created_at")

    def validate_text(self, value):
        if len(value) == 0:
            raise serializers.ValidationError(
                detail="The field text should be filled"
            )
        return value


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "question_id", "text", "created_at", "user_id")


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "text", "created_at", "answers")

    def validate_text(self, value):
        if len(value) == 0:
            raise serializers.ValidationError(
                detail="The field text should be filled"
            )
        return value
