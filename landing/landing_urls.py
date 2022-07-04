from django.urls import path


from landing import views


urlpatterns = [
    path("", views.landing),
    path("base/", views.base),
    path("extends/", views.extends),
]
