from django.shortcuts import render


from vacancyapp.models import Vacancy
from resumeapp.models import Resume


def main_list(request):
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False, is_active=True)
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(is_draft=False, is_active=True)
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data}
    return render(request, 'mainapp/main.html', context)
