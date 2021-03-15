from django.shortcuts import render


from Vacancy.models import Vacancy
from resume.models import Resume


def main_list(request):
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False)
        # data = Resume.objects.all()
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(draft=False)
        # data = Vacancy.objects.all()
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data}
    return render(request, 'mainapp/main.html', context)
