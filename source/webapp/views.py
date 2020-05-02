from django.http import HttpResponse
from django.shortcuts import render

from webapp.models import Post, Like


def index(request):
    posts = Post.objects.all()
    return render(request, 'webapp/core/post.html', {'posts': posts})

def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedPost = Post.objects.get(pk=post_id)
        m = Like(post=likedPost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET")