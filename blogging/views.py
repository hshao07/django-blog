from django.shortcuts import render
from django.http import Http404
from blogging.models import Post

def list_view(request):
    context = {'post': Post.objects.all()}
    return render(request, 'blogging/list.html', context)
