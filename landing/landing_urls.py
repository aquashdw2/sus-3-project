from django.urls import path


from landing import views


urlpatterns = [
    path("", views.homepage),
    path("templates/", views.landing),
    path("base/", views.base),
    path("extends/", views.extends),
]
