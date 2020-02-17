#django
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

#models
from posts.models import Post
#forms
from posts.forms import PostForm

@login_required
def list_post(request):
    #list existing post
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    #create new post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
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
