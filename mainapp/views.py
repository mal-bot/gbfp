from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from mainapp.models import BlogPost, Favorites
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
    page = request.GET.get('page')
    paginator = Paginator(data, 5)
    try:
        data_paginator = paginator.page(page)
    except PageNotAnInteger:
        data_paginator = paginator.page(1)
    except EmptyPage:
        data_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'page': page,
        'data': data_paginator,
    }
    return render(request, 'mainapp/vacancy_list.html', context)


def invite(request, pk):
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Responses.objects.get(resume=resume,
                                      user=user)
        if not check:
            Responses.objects.create(resume=resume,
                                     user=user)
        elif not check.is_active:
            check.is_active = True
            check.save()
        else:
            check.is_active = False
            check.save()
    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Responses.objects.get(vacancy=vacancy,
                                      user=user)
        if not check:
            Responses.objects.create(vacancy=vacancy,
                                     user=user)
        elif not check.is_active:
            check.is_active = True
            check.save()
        else:
            check.is_active = False
            check.save()
    return vac_res_list(request)


def favorites(request, pk):
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Favorites.objects.get(resume=resume,
                                      user=user)
        if not check:
            Favorites.objects.create(resume=resume,
                                     user=user)
        elif not check.is_active:
            check.is_active = True
            check.save()
        else:
            check.is_active = False
            check.save()

    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        check = Favorites.objects.get(vacancy=vacancy,
                                      user=user)
        if not check:
            Favorites.objects.create(vacancy=vacancy,
                                     user=user)
        elif not check.is_active:
            check.is_active = True
            check.save()
        else:
            check.is_active = False
            check.save()
    return vac_res_list(request)
