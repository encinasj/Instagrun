# Django
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

#exceptions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile
def login_views(request):
    #Login views
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
             return render(request,'users/login.html', {'error': 'Invaid username and password'})

    return render(request, 'users/login.html')

def signup(request):
    #sign up view
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmatin doest not mach' })
        
        try:
            user = User.objects.create_user(username=username, password=passwd)        
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user' })

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('login')

    return render(request,'users/signup.html')

def update_profile(request):
    #Update a users profile views
    return render(request,'users/update_profile.html')
    
@login_required
def logout_views(request):
    #loout_views
    logout(request)
    return redirect('login')
