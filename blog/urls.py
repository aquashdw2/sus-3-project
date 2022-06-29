from django.urls import path

from blog import views


# blog/urls.py
urlpatterns = [
    path("home/", views.blog_home),
    path("create/", views.blog_post_create),
    path("read/", views.blog_post_read),
    path("update/", views.blog_post_update),
    path("delete/", views.blog_post_delete),
]
