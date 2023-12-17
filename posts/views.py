# from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy  #handle redirection to homepage
from .forms import PostForm  #allow users to upload the images via a form
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')