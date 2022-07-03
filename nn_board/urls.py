from django.urls import path

from nn_board import views


urlpatterns = [
    path("home/", views.home),
    path("post/create/", views.post_create),
    path("post/<int:target_id>/read/", views.post_read),
    path("post/<int:target_id>/update/", views.post_update),
    path("post/<int:target_id>/delete/", views.post_delete),
]
