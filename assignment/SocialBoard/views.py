from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'SocialBoard/posts.html', {'posts':posts})
