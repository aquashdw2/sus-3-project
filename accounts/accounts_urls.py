from django.urls import path

from accounts import views


app_name = "accounts-url-name"
urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("sign-in/", views.sign_in, name="sign-in"),
    path("sign-out", views.sign_out, name="sign-out"),
    path("logged-in/", views.logged_in, name="logged-in")
]
