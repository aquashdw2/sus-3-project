from django.urls import path

from blog import views


# blog/urls.py
urlpatterns = [
    path("home/", views.blog_home),
    path("create/", views.post_create),
    path("read/", views.post_read),
    path("update/", views.post_update),
    path("delete/", views.post_delete),
]
