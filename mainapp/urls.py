from django.urls import path
from django.views.generic import TemplateView

import mainapp.views as mainapp

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mainapp/main.html'), name='main'),
    path('list/', mainapp.main_list, name='main_list'),
]
