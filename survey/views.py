from django.shortcuts import render, redirect

from survey.models import SurveySimple, SurveyChoices


def create_survey_simple(request):
    if request.method == "POST":
        
        print(request.POST.get("age"))
        print(request.POST.get("gender"))
        print(request.POST.get("address"))
        print(request.POST.get("suggestion"))
        return redirect("/polls/submit-simple/")
    elif request.method == "GET":
        return render(request, "polls/simple.html")


def create_survey_choice(request):
    if request.method == "POST":
        print(request.POST.get("age"))
        print(request.POST.get("gender"))
        print(request.POST.get("address"))
        print(request.POST.get("suggestion"))
        return redirect("/polls/submit-choice/")
    elif request.method == "GET":
        return render(request, "polls/choice.html")
