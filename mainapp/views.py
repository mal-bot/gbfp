from django.shortcuts import render
from mainapp.models import BlogPost
from authapp.models import User
from vacancyapp.models import Vacancy
from resumeapp.models import Resume
from mainapp.models import Responses


def main_list(request):
    blog_posts = BlogPost.objects.all()
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False, is_active=True)
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(draft=False, is_approved=True)
        # data = vacancyapp.objects.all()
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data,
        'blog_posts': blog_posts}
    return render(request, 'mainapp/vacancy_list.html', context)

  
def invite(request, pk):
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

