from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm



def register(request):
    form = UserCreationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post_list')
    context = {
        'form': form
    }
    return render(request, 'Registration/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #first_name = request.POST['first_name']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('post_list')
        else:
            error = 'username or password incorrect'
            return render(request, 'Registration/login.html', {'error': error})
    else:
        return render(request, 'Registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')