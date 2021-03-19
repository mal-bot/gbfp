from django.urls import path

import companyapp.views as personalarea

app_name = 'company'

urlpatterns = [
    path('', personalarea.IndexView.as_view(extra_context={'title': 'Личный кабинет'}), name='view'),
    path('company/update/<int:pk>', personalarea.CompanyUpdateView.as_view(), name='company_update'),
    path('company/detail/<int:pk>', personalarea.CompanyDetailView.as_view(), name='company_detail'),
]