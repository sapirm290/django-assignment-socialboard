from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
import json


@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'SocialBoard/main.html', {'posts': posts})

@require_http_methods(['POST'])
def create_post(request):
    # try:
    post_date = json.loads(request.body)
    new_post = Post(title=post_date["title"],
                    content=post_date["content"], author=post_date["author"])
    new_post.save()
    return HttpResponse('success', status=201)
    # except Exception as ex:
    #     return HttpResponse('error', status=500)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'
