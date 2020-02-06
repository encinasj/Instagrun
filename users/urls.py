#django
from django.urls import path
from users.views import login_views

users_urlpatterns = [
    path('login/', login_views, name='login'),
]
