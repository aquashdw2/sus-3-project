from django.urls import path


from boot import views


app_name = "boot"
urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("sign-in/", views.sign_in, name="sign-in")
]
