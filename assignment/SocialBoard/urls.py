from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('create_post', views.create_post, name='create_post'),
    path('signup', views.SignUp.as_view(), name='signup'),

]
