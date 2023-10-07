from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
    )
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AboutView(TemplateView):
    template_name = 'about.html'
