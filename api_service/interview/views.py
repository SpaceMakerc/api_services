from django.shortcuts import render, HttpResponse, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from interview.models import Question
from interview.serializers import QuestionSerializer, QuestionsSerializer


@api_view(http_method_names=["GET", "POST"])
def api_questions(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)


@api_view(http_method_names=["GET"])
def api_question_detail(request, pk: int):
    question = get_object_or_404(Question, pk=pk)
    print(question)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)

