from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
        posts = Post.objects.all().order_by("-created")
        return render(request, "blog/index.html", { "posts" : posts })


def blog_view(request, blog_id):
    return render(request, "blog/blog_view.html", { "post" : get_object_or_404(Post, pk = int(blog_id)) , "posts" : Post.objects.all().order_by("-created")})
