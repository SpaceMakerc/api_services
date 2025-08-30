from rest_framework import serializers

from interview.models import Question, Answer


class QuestionsSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {
            "text": {
                "error_messages": {
                    "required": "Question field cannot be empty",
                },
            },
            "user_id": {
                "error_messages": {
                    "required": "user_id field cannot be empty",
                },
            },
            "question_id": {
                "error_messages": {
                    "required": "user_id field cannot be empty",
                },
            }
        }


class QuestionSerializer(QuestionsSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta(QuestionsSerializer.Meta):
        model = Question
        fields = ("id", "text", "created_at", "answers")
