from django.urls import path
from posts.views import list_post

post_urlpatterns = [
    path('', list_post, name='posts'),
]
