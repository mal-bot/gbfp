from django.shortcuts import render


from vacancyapp.models import Vacancy
from resumeapp.models import Resume


def main_list(request):
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False)
        # data = Resume.objects.all()
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(draft=False)
        # data = vacancyapp.objects.all()
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data}
    return render(request, 'mainapp/main.html', context)
