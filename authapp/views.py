from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth
from authapp.forms import UserLoginForm, ApplicantRegistrationForm, CompanyRegistrationForm


def login(request):
    print(request.user.username)
    title = 'вход'

    next = request.GET.get('next', '')

    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main:main_list'))
    else:
        form = UserLoginForm()

    content = {'title': title, 'form': form,
               'next': next}
    return render(request, 'registration/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main_list'))


def register(request, reg_type='applicant'):
    title = 'Регистрация соискателя' if reg_type == 'applicant' else 'Регистрация работодателя'

    if reg_type == 'company':
        form = CompanyRegistrationForm(data=request.POST)
    else:
        form = ApplicantRegistrationForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            if reg_type == 'company':
                user.is_staff = True
                user.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        if reg_type == 'company':
            form = CompanyRegistrationForm()
        else:
            form = ApplicantRegistrationForm()


    content = {
        'title': title,
        'form': form,
        'reg_type': reg_type
    }
    return render(request, 'registration/register.html', content)
