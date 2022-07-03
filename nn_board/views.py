from django.shortcuts import render, redirect

from nn_board.models import BoardPost


def home(request):
    post_all = BoardPost.objects.all().order_by("-pk")
    context = {
        "post_list": post_all
    }
    return render(
        request,
        "nn-board/index.html",
        context
    )


def post_create(request):
    if request.method == "POST":
        new_post = BoardPost()
        new_post.title = request.POST.get("title")
        new_post.content = request.POST.get("content")
        new_post.username = request.POST.get("username")
        new_post.password = request.POST.get("password")
        new_post.save()
        
        return redirect("/nn-board/home/")
    elif request.method == "GET":
        return render(request, "nn-board/post-create.html")


def post_read(request, target_id):
    target_post = BoardPost.objects.get(id=target_id)
    context = {
        "post": target_post,
    }
    return render(
        request, 
        "nn-board/post-read.html",
        context
    )


def post_update(request, target_id):
    target_post = BoardPost.objects.get(id=target_id)
    if request.method == "POST":
        if not (target_post.username == request.POST.get("username") \
            and target_post.password == request.POST.get("password")):
            return redirect(f"/nn-board/post/{target_id}/update/") 
        target_post.title = request.POST.get("title")
        target_post.content = request.POST.get("content")
        target_post.save()

        return redirect(f"/nn-board/post/{target_id}/read/")

    elif request.method == "GET":
        context = {
            "post": target_post,
        }

        return render(
            request,
            "nn-board/post-update.html", 
            context
        )


def post_delete(request, target_id):
    target_post = BoardPost.objects.get(id=target_id)
    if request.method == "POST":
        if not (target_post.username == request.POST.get("username") \
            and target_post.password == request.POST.get("password")):
            return redirect(f"/nn-board/post/{target_id}/delete/") 
        target_post.delete()
        return redirect("/nn-board/home/")
    elif request.method == "GET":
        context = {
            "post": target_post
        }
        return render(
            request, 
            "nn-board/post-delete.html",
            context
        )
