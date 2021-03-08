from django.urls import path

import personalareaapp.views as personalarea

app_name = 'personalarea'

urlpatterns = [
    path('', personalarea.IndexView.as_view(extra_context={'title': 'Личный кабинет'}), name='view'),
]