from django.urls import path

from interview import views


urlpatterns = [
    path(
        "questions/", views.APIQuestions.as_view(),
        name="get_post_question"
    ),
    path(
        "questions/<int:id>", views.APIQuestion.as_view(),
        name="get_delete_questions"
    ),
    path(
        "questions/<int:id>/answers/", views.APIAnswers.as_view(),
        name="post_answer"
    ),
    path("answers/<int:id>/", views.APIAnswer.as_view())
]
