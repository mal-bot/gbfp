from django.urls import path

from vacancyapp import views

app_name = 'vacancy'

urlpatterns = [
    path('', views.VacancyListView.as_view(), name='vacancy_list'),
    path('create/', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('update/<int:pk>/', views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('delete/<int:pk>/', views.VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('detail/<int:pk>/', views.VacancyDetailView.as_view(), name='vacancy_detail'),
]
