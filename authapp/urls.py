from django.urls import path, include

app_name = 'auth'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
