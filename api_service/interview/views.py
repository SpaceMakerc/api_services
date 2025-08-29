from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from interview.models import Question
from interview.serializers import QuestionSerializer, QuestionsSerializer


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
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        Question.delete(question)
        return Response(
            data={
                "data": {
                    "question_id": pk,
                    "question_text": question.text,
                    "Deleted": True
                }
            },
            status=status.HTTP_200_OK
        )
