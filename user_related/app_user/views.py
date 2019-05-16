from django.shortcuts import render
from app_user.forms import UserForm, UserProfileInfoForm

#import for login
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    return render(request, 'index.html', {'index':"Hello users, we'll be doing about users stuffs here in this project."})

@login_required
def special(request):
    return render(request, 'app_user/special.html',{'special':"You are logged in, Nice!"})

@login_required
def u_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):

    registered = False
    print(registered)
    if request.method == 'POST':
        print('checkpoint if')
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
            print(registered)
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        print('checkpoint else')
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_user/registration.html',
                                   {'user_form':user_form,
                                    'profile_form': profile_form,
                                    'registered':registered })

def u_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app_user:special'))
            else:
                return HttpResponse("Account not active")
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password {}'.format(username, password))
    else:
        return render(request, 'app_user/login.html', {})