from django.shortcuts import render, get_object_or_404

from .models import Post

def blog(request):

    c = {}

    c['user'] = request.user
    c['latest_post'] = Post.objects.latest('created_at')
    c['posts'] = Post.objects.all()

    return render(request, 'blog.html', c)

def post(request, slug):

    post = get_object_or_404(Post, slug = slug)

    c = {}
    c['user'] = request.user
    c['post'] = post

    return render(request, 'post.html', c)