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
        return render(request, "survey/create-simple.html")


def read_all_survey_simple(request):
    survey_list = SurveySimple.objects.all()
    context = {
        "survey_list": survey_list,
        "survey_count": len(survey_list),
    }
    return render(request, "survey/results-simple.html", context)


def read_survey_simple(request, survey_id):
    survey = SurveySimple.objects.get(id=survey_id)
    context = {
        "survey": survey
    }
    return render(request, "survey/results-simple-one.html", context)


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
        return render(request, "survey/create-choice.html")


def read_all_survey_choice(request):
    survey_list = SurveyChoices.objects.all()
    context = {
        "survey_list": survey_list,
        "survey_count": len(survey_list),
    }
    return render(request, "survey/results-choice.html", context)


def read_survey_choice(request, survey_id):
    survey = SurveyChoices.objects.get(id=survey_id)
    context = {
        "survey": survey
    }
    return render(request, "survey/results-choice-one.html", context)
