from django.urls import path

import personalareaapp.views as personalarea
from Vacancy import views

app_name = 'personalarea'

urlpatterns = [
    path('', personalarea.IndexView.as_view(extra_context={'title': 'Личный кабинет'}), name='view'),

    path('vacancy/create/', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/update/<int:pk>/', views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/delete/<int:pk>/', views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]