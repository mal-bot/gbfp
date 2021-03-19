from django.shortcuts import render
from authapp.models import User
from vacancyapp.models import Vacancy
from resumeapp.models import Resume
from mainapp.models import Responses


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


def invite(request, pk):
    # data = Responses.objects.all()
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()

        Responses.objects.create(resume=resume,
                                 user=user)

    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()

        Responses.objects.create(vacancy=vacancy,
                                 user=user)

    return main_list(request)
