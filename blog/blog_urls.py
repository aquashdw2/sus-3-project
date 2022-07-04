from django.urls import path

from blog import views


app_name = "blog"
urlpatterns = [
    path("home/", views.blog_home, name="home"),
    path("create/", views.blog_post_create, name="create"),
    path("<int:target_id>/read/", views.blog_post_read, name="read"),
    path("<int:target_id>/update/", views.blog_post_update, name="update"),
    path("<int:target_id>/delete/", views.blog_post_delete, name="delete"),
    path("<int:foo>/<int:bar>/<int:baz>/", views.foo_bar_baz, name="demo"),
]
