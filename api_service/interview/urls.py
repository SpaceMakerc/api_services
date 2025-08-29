from django.urls import path

from interview import views


urlpatterns = [
    path("questions/", views.APIQuestions.as_view()),
    path("questions/<int:id>/", views.APIQuestion.as_view()),
    path("questions/<int:id>/answers/", views.APIAnswers.as_view()),
    path("answers/<int:id>/", views.APIAnswer.as_view())
]
