from django.urls import path

from survey import views


urlpatterns = [
    path("submit-simple/", views.create_survey_simple),
    path("result-simple/", views.read_all_survey_simple),
    path("result-simple/<int:survey_id>/", views.read_survey_simple),
    path("submit-choice/", views.create_survey_choice),
    path("result-choice/", views.read_all_survey_choice),
    path("result-choice/<int:survey_id>/", views.read_survey_choice),
]
