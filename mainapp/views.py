from django.shortcuts import render
from mainapp.models import BlogPost
from authapp.models import User
from vacancyapp.models import Vacancy
from resumeapp.models import Resume
from mainapp.models import Responses


def main_news(request):
    blog_posts = BlogPost.objects.all()
    company_list = User.objects.filter(is_partner=True)
    context = {
        'blog_posts': blog_posts,
        'company_list': company_list,
    }
    return render(request, 'mainapp/main.html', context)


def vac_res_list(request):
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False, is_active=True, is_approved=True)
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(is_draft=False, is_active=True, is_approved=True)
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data,
    }
    return render(request, 'mainapp/vacancy_list.html', context)


def invite(request, pk):
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Responses.objects.filter(resume=resume,
                                         user=user)
        if not check:
            Responses.objects.create(resume=resume,
                                     user=user)

    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Responses.objects.filter(vacancy=vacancy,
                                         user=user)
        if not check:
            Responses.objects.create(vacancy=vacancy,
                                     user=user)
    return vac_res_list(request)
