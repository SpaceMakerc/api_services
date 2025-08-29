from django.urls import path

from interview import views


urlpatterns = [
    path("questions/", views.api_questions),
    path("questions/<int:pk>/", views.api_question_detail)
]
