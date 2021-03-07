from django.conf.urls import url
from django.urls import path, include

import authapp.views as authapp

app_name = 'auth'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', authapp.login, name='login'),
    # path('register/<str:reg_type>/', authapp.register, name='register'),
    url(r'^register/(?P<reg_type>\w{0,50})/$', authapp.register, name='register'),

]
