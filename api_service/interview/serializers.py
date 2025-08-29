from rest_framework import serializers

from datetime import datetime

from interview.models import Question, Answer


class QuestionsSerializer(serializers.ModelSerializer):
    def validate(self, data):
        try:
            new_date = datetime.fromisoformat(data)
        except TypeError:
            raise serializers.ValidationError(
                detail="Date field should be 'YYYY-MM-DD' type or None"
            )
        return data

    class Meta:
        model = Question
        fields = ("id", "text", "created_at")
        extra_kwargs = {
            "text": {
                "error_messages": {
                    "required": "Question field cannot be empty",
                },
            },
        }


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "question_id", "text", "created_at", "user_id")


class QuestionSerializer(QuestionsSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta(QuestionsSerializer.Meta):
        model = Question
        fields = ("id", "text", "created_at", "answers")
