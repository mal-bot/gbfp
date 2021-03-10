from django.urls import path

import personalareaapp.views as personalarea

app_name = 'personalarea'

urlpatterns = [
    path('', personalarea.IndexView.as_view(extra_context={'title': 'Личный кабинет'}), name='view'),
    path('company/update/<int:pk>', personalarea.CompanyUpdateView.as_view(), name='company_update'),
    path('user/update/<int:pk>', personalarea.UserUpdateView.as_view(), name='user_update'),
]