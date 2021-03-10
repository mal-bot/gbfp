from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Vacancy.forms import VacancyEditForm
from Vacancy.models import Vacancy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


class VacancyListView(ListView):
    model = Vacancy
    paginate_by = 10
    title = 'Вакансии'
    ordering = '-is_active'
    # template_name = 'vacancy/vacancy_list.html'
    template_name = 'personalareaapp/pa_content.html'

    # def test_func(self):
    #     return self.request.user.is_staff

    # def handle_no_permission(self):
    #     return HttpResponseRedirect(reverse('main'))


class VacancyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vacancy
    success_url = reverse_lazy('personalarea:view')
    form_class = VacancyEditForm
    title = 'Создать вакансию'
    template_name = 'vacancy/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main'))


class VacancyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacancy
    success_url = reverse_lazy('personalarea:view')
    form_class = VacancyEditForm
    title = 'Редактировать вакансию'
    template_name = 'vacancy/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyUpdateView, self).form_valid(form)

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main'))


class VacancyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacancy
    success_url = reverse_lazy('personalarea:view')
    title = 'Удалить вакансию'
    template_name = 'vacancy/vacancy_confirm_delete.html'

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main'))