from django.urls import path
import mainapp.views as mainapp

app_name = 'main'

urlpatterns = [
    path('', mainapp.main_list, name='main_list'),
]
