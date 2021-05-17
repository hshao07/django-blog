from django.urls import path
from blogging.views import list_view

urlpatterns = [
    path('', list_view, name="post_index"),
]