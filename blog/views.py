from django.shortcuts import render, redirect

from blog.models import Article


def blog_home(request):
    post_all = Article.objects.all().order_by("-pk")

    context = {
        "post_list": post_all
    }
    return render(
        request,
        "blog-html/index.html",
        context
    )


def blog_post_create(request):
    if request.method == "POST":
        new_post = Article()
        new_post.title = request.POST.get("title")
        new_post.content = request.POST.get("content")
        new_post.save()
        
        return redirect("blog:home")
    elif request.method == "GET":
        return render(request, "blog-html/post-create.html")


def blog_post_read(request, target_id):
    target_post = Article.objects.get(id=target_id)
    context = {
        "post": target_post,
    }
    return render(
        request, 
        "blog-html/post-read.html",
        context
    )


def blog_post_update(request, target_id):
    target_post = Article.objects.get(id=target_id)
    if request.method == "POST":
        target_post.title = request.POST.get("title")
        target_post.content = request.POST.get("content")
        target_post.save()

        return redirect("blog:read", target_id)

    elif request.method == "GET":
        context = {
            "post": target_post,
        }

        return render(
            request,
            "blog-html/post-update.html", 
            context
        )


def blog_post_delete(request, target_id):
    target_post = Article.objects.get(id=target_id)
    if request.method == "POST":
        target_post.delete()
        return redirect("blog:home")
    elif request.method == "GET":
        context = {
            "post": target_post
        }
        return render(
            request, 
            "blog-html/post-delete.html",
            context
        )


def foo_bar_baz(request, foo, bar, baz):
    print(foo)
    print(bar)
    print(baz)
    return redirect("blog:home")
