from django.urls import path

import personalareaapp.views as personalarea

app_name = 'personalarea'

urlpatterns = [
    path('', personalarea.personal_area, name='view'),
]