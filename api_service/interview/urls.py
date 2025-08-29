from django.urls import path

from interview import views


urlpatterns = [
    path("questions/", views.APIQuestions.as_view()),
    path("questions/<int:pk>/", views.APIQuestion.as_view())
]
