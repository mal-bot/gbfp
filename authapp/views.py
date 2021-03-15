from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.views.generic import CreateView

from authapp.forms import UserLoginForm, ApplicantRegistrationForm, CompanyRegistrationForm
from authapp.models import User


class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = UserLoginForm


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main_list'))


class ApplicantRegistration(CreateView):
    form_class = ApplicantRegistrationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'registration/register.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reg_type'] = self.kwargs['reg_type']
    #     return context


class CompanyRegistration(CreateView):
    form_class = CompanyRegistrationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.is_staff = True
        return super(CompanyRegistration, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reg_type'] = self.kwargs['reg_type']
    #     return context

# def register(request, reg_type='applicant'):
#     title = 'Регистрация соискателя' if reg_type == 'applicant' else 'Регистрация работодателя'
#
#     if reg_type == 'company':
#         form = CompanyRegistrationForm(data=request.POST)
#     else:
#         form = ApplicantRegistrationForm(data=request.POST)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             if reg_type == 'company':
#                 user.is_staff = True
#                 user.save()
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         if reg_type == 'company':
#             form = CompanyRegistrationForm(data=request.POST)
#         else:
#             form = ApplicantRegistrationForm(data=request.POST)
#
#     content = {
#         'title': title,
#         'form': form,
#         'reg_type': reg_type
#     }
#     return render(request, 'registration/register.html', content)

