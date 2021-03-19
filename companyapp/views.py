from django.views.generic import ListView, UpdateView, DetailView
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from mainapp.models import Responses
from vacancyapp.models import Vacancy
from authapp.models import User
from companyapp.forms import UserEditForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse


# @method_decorator(login_required(), name='dispatch')
class IndexView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'companyapp/pa_content.html'
    model = Vacancy
    # context_object_name = 'vacancies_list'
    # queryset = vacancyapp.objects.filter()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['vacancies_list'] = Vacancy.objects.filter(company_id=self.request.user.pk)
        # print(context['resume_list'])
        context['responses_list'] = Responses.objects.all()
        context['title'] = 'Личный кабинет'
        return context

    # def get_queryset(self):
    #     return self.model.objects.filter(company=self.request.user.pk)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))


# @method_decorator(login_required(), name='dispatch')
class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    success_url = reverse_lazy('company:view')
    form_class = UserEditForm
    title = 'Редактировать данные профиля'
    template_name = 'companyapp/company_form.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))


class CompanyDetailView(DetailView):
    model = User
    title = 'Компания'
    template_name = 'companyapp/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['vacancies_list'] = Vacancy.objects.filter(company_id=self.kwargs['pk'], is_active=True)
        return context