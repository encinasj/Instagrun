#django
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
#models
from posts.models import Post
#forms
from posts.forms import PostForm

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',) 
    '''pagination'''
    paginate_by = 10          
    context_object_name = 'posts'

class PostsDetailView(LoginRequiredMixin, DeleteView):
    '''return detail posts'''
    template_name='posts/detail.html'
    queryset= Post.objects.all()
    context_object_name='post'

@login_required
def create_post(request):
    #create new post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile':request.user.profile

        }
    )
     