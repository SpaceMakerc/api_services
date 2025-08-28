from django.urls import path

from interview.views import *


urlpatterns = [
    path("", index, name="index_page")
]
