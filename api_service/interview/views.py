from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from interview.models import Question, Answer
from interview.serializers import (
    QuestionSerializer,
    QuestionsSerializer,
    AnswerSerializer
)


class APIQuestions(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(
            data=serializer.data, status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class APIQuestion(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def delete(self, request, id):
        question = get_object_or_404(Question, pk=id)
        Question.delete(question)
        return Response(
            data={
                "data": {
                    "question_id": id,
                    "question_text": question.text,
                    "Deleted": True
                }
            },
            status=status.HTTP_200_OK
        )


class APIAnswers(APIView):
    def post(self, request, id):
        get_object_or_404(Question, pk=id)
        request_data = {}
        for key, value in request.data.items():
            request_data[key] = value
        request_data["question_id"] = id
        serializer = AnswerSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class APIAnswer(APIView):
    def get(self, request, id):
        answer = get_object_or_404(Answer, pk=id)
        serializer = AnswerSerializer(answer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        answer = get_object_or_404(Answer, pk=id)
        Answer.delete(answer)
        return Response(
            data={
                "data": {
                    "anser_id": id,
                    "question_text": answer.text,
                    "user_id": answer.user_id,
                    "Deleted": True
                }
            },
            status=status.HTTP_200_OK
        )
