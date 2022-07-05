from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("accounts-url-name:logged-in")
    context = {}
    if request.method == "POST":
        username_input = request.POST.get("username")
        password_input = request.POST.get("password")
        password_check_input = request.POST.get("password_check")
        if username_input and \
            password_input and \
            password_input == password_check_input:

            if User.objects.filter(username=username_input).exists():
                context["error"] = "사용중인 아이디 입니다."

            else:
                new_user = User.objects.create_user(
                    username=username_input,
                    password=password_input,
                )

                auth.login(request, new_user)

                return redirect("accounts-url-name:logged-in")
        else:
            context["error"] = "올바르지 않은 정보입니다."
            
    return render(request, "accounts-html/sign-up.html", context)


def sign_in(request):
    context = {}
    if request.method == "POST":
        username_input = request.POST.get("username")
        password_input = request.POST.get("password")
        if username_input and password_input:
            sign_in_user = auth.authenticate(
                request, 
                username=username_input,
                password=password_input,
            )

            if sign_in_user is not None:
                auth.login(request, sign_in_user)
                return redirect("accounts-url-name:logged-in")
            else:
                context["error"] = "해당하는 사용자가 없습니다."
        else:
            context["error"] = "아이디와 비밀번호를 입력해주세요."

    return render(request, "accounts-html/sign-in.html", context)


def sign_out(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("accounts-url-name:logged-in")


def logged_in(request):
    context = {
        "logged_in": request.user.is_authenticated,
    }
    return render(request, "accounts-html/logged-in.html", context)
