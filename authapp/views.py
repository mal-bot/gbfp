from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

from authapp.forms import UserLoginForm


def login(request):
    title = 'вход'

    next = request.GET.get('next', '')

    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main:home'))
    else:
        login_form = UserLoginForm()

    content = {'title': title, 'login_form': login_form,
               'next': next}
    return render(request, 'registration/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:home'))

# Create your views here.
