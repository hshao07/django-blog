from django.shortcuts import render
from blogging.models import Post
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.filter(published_date__exact=None)
    queryset = Post.objects.order_by("-published_date")
