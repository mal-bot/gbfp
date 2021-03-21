from django.shortcuts import render

from mainapp.models import BlogPost
from vacancyapp.models import Vacancy
from resumeapp.models import Resume


def main_list(request):
    blog_posts = BlogPost.objects.all()
    if request.user.is_staff:
        data = Resume.objects.filter(is_draft=False)
        # data = Resume.objects.all()
        title = 'Список резюме'
    else:
        data = Vacancy.objects.filter(draft=False, is_approved=True)
        # data = vacancyapp.objects.all()
        title = 'Список вакансий'
    context = {
        'title': title,
        'data': data,
        'blog_posts': blog_posts}
    return render(request, 'mainapp/main.html', context)
