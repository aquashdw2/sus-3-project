from django.urls import path

from polls import views


urlpatterns = [
    path("submit-simple/", views.create_survey_simple),
    path("submit-choice/", views.create_survey_choice)
]
