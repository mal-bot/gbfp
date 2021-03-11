from django.urls import path

import applicantapp.views as applicant

app_name = 'applicant'

urlpatterns = [
    path('', applicant.ResumeList.as_view(), name='view'),
    path('update/<int:pk>', applicant.ApplicantUpdateView.as_view(), name='applicant_update'),
]