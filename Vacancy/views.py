from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Vacancy.forms import VacancyEditForm
from Vacancy.models import Vacancy


class VacancyListView(ListView):
    model = Vacancy
    paginate_by = 10
    title = 'Вакансии'
    ordering = '-is_active'
    template_name = 'vacancy/vacancy_list.html'


class VacancyCreateView(CreateView):
    model = Vacancy
    success_url = reverse_lazy('vacancy:vacancy_list')
    form_class = VacancyEditForm
    title = 'Создать вакансию'
    template_name = 'vacancy/vacancy_form.html'


class VacancyUpdateView(UpdateView):
    model = Vacancy
    success_url = reverse_lazy('vacancy:vacancy_list')
    form_class = VacancyEditForm
    title = 'Редактировать вакансию'
    template_name = 'vacancy/vacancy_form.html'


class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancy:vacancy_list')
    title = 'Удалить вакансию'
    template_name = 'vacancy/vacancy_confirm_delete.html'
