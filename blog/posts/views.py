from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(req):

    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(req, 'index.html', context)

def post(req, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(req, 'post.html', context)
