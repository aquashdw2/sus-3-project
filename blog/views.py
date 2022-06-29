from django.shortcuts import render

from blog.models import BlogPost


def blog_home(request):
    return render(request, "blog/index.html")


def post_create(request):
    return render(request, "blog/post-create.html")


def post_read(request):
    return render(request, "blog/post-read.html")


def post_update(request):
    return render(request, "blog/post-update.html")


def post_delete(request):
    return render(request, "blog/post-delete.html")


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
