from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from mainapp.models import Responses
from vacancyapp.forms import VacancyEditForm
from vacancyapp.models import Vacancy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


class VacancyListView(ListView):
    model = Vacancy
    paginate_by = 10
    title = 'Вакансии'
    ordering = '-is_active'
    template_name = 'companyapp/pa_content.html'


class VacancyDetailView(DetailView):
    model = Vacancy
    title = 'Вакансия'
    template_name = 'vacancyapp/vacancy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_responses'] = False
        response = Responses.objects.filter(vacancy_id=self.kwargs['pk'], user_id=self.request.user.pk)
        if response:
            context['in_responses'] = True
        return context


class VacancyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vacancy
    success_url = reverse_lazy('company:view')
    form_class = VacancyEditForm
    title = 'Создать вакансию'
    template_name = 'vacancyapp/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))


class VacancyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacancy
    success_url = reverse_lazy('company:view')
    form_class = VacancyEditForm
    title = 'Редактировать вакансию'
    template_name = 'vacancyapp/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyUpdateView, self).form_valid(form)

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))


class VacancyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacancy
    success_url = reverse_lazy('company:view')
    title = 'Удалить вакансию'
    template_name = 'vacancyapp/vacancy_confirm_delete.html'

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))

