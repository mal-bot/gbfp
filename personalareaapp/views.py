from django.views.generic import ListView, UpdateView
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Vacancy.models import Vacancy
from authapp.models import User
from personalareaapp.forms import UserEditForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse


# @method_decorator(login_required(), name='dispatch')
class IndexView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'personalareaapp/pa_content.html'
    model = Vacancy
    context_object_name = 'vacancies_list'
    # queryset = Vacancy.objects.filter()

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     # context['favourites_list'] = [1, 2, 3]
    #     # context['user'] = {'name': 'Иван'}
    #     return context

    def get_queryset(self):
        return self.model.objects.filter(company=self.request.user.pk)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main'))


# @method_decorator(login_required(), name='dispatch')
class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    success_url = reverse_lazy('personalarea:view')
    form_class = UserEditForm
    title = 'Редактировать данные профиля'
    template_name = 'personalareaapp/company_form.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main'))


class UserUpdateView(UpdateView):
    pass