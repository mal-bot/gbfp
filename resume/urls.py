from django.urls import path

from resume import views

app_name = 'resume'

urlpatterns = [
    path('', views.ResumeListView.as_view(), name='resume_list'),
    path('create/', views.ResumeCreateView.as_view(), name='resume_create'),
    path('update/<int:pk>/', views.ResumeUpdateView.as_view(), name='resume_update'),
    path('delete/<int:pk>/', views.ResumeDeleteView.as_view(), name='resume_delete'),
    path('detail/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail'),
]
