from django.shortcuts import render
from Blog.models import Post


def blog(request):

    posts = Post.objects.all()

    return render(request, "Blog/blog.html", {"posts": posts})
