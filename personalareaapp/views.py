from django.views.generic import ListView

from Vacancy.models import Vacancy


class IndexView(ListView):
    template_name = 'personalareaapp/pa_content.html'
    model = Vacancy
    context_object_name = 'vacancies_list'
    queryset = Vacancy.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['favourites_list'] = [1, 2, 3]
        context['user'] = {'name': 'Иван'}
        return context
