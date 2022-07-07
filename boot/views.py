from django.shortcuts import render, redirect
from django.contrib import auth


def index(request):
    return render(request, "boot/index.html")


def contact(request):
    return render(request, "boot/contact.html")


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
                return redirect("boot:home")
            else:
                context["error"] = "해당하는 사용자가 없습니다."
        else:
            context["error"] = "아이디와 비밀번호를 입력해주세요."

    return render(request, "boot/sign-in.html")
