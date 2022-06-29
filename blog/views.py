from django.shortcuts import render, redirect

from blog.models import BlogPost


def blog_home(request):
    return render(request, "blog-html/index.html")


def post_create(request):
    if request.method == "POST":
        new_post = BlogPost()
        new_post.title = request.POST.get("title")
        new_post.content = request.POST.get("content")
        new_post.save()
        
        return redirect("/blog-url/home/")
    elif request.method == "GET":
        return render(request, "blog-html/post-create.html")


def post_read(request):
    return render(request, "blog-html/post-read.html")


def post_update(request):
    return render(request, "blog-html/post-update.html")


def post_delete(request):
    return render(request, "blog-html/post-delete.html")


def temp():
    # Create
    new_post = BlogPost()
    new_post.title = "new post title"
    new_post.content = "Lorem Ipsum"
    new_post.save()


    # Read
    post_list = BlogPost.objects.all()
    for post in post_list:
        print(post.title)
    first_post = BlogPost.objects.get(id=1)
    print(f"title: {first_post.title}")
    print(f"content: {first_post.content}")
    print(f"created: {first_post.created_at}")


    # Update
    target_post = BlogPost.objects.get(id=3)
    target_post.title = "Blog Title 3"
    target_post.content = "new updated content"
    target_post.save()


    # Delete
    target_post = BlogPost.objects.order_by("-pk")[0]
    target_post.delete()
