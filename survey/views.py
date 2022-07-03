from django.shortcuts import render, redirect

from survey.models import SurveySimple, SurveyChoices


def create_survey_simple(request):
    if request.method == "POST":
        new_survey = SurveySimple()
        new_survey.age = request.POST.get("age")
        new_survey.gender = request.POST.get("gender")
        new_survey.address = request.POST.get("address")
        new_survey.suggestions = request.POST.get("suggestions")
        new_survey.save()

        return redirect("/survey/submit-simple/")
    elif request.method == "GET":
        return render(request, "polls/simple.html")


def create_survey_choice(request):
    if request.method == "POST":
        new_survey = SurveyChoices()
        new_survey.age = request.POST.get("age")
        new_survey.gender = request.POST.get("gender")
        new_survey.address = request.POST.get("address")
        new_survey.suggestions = request.POST.get("suggestions")
        new_survey.save()

        return redirect("/survey/submit-choice/")
    elif request.method == "GET":
        return render(request, "polls/choice.html")
