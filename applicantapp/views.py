from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from applicantapp.forms import ApplicantEditForm
from authapp.models import User
from resumeapp.models import Resume


class ResumeList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'applicantapp/applicant_content.html'
    model = Resume
    context_object_name = 'resume_list'

    def get_context_data(self, **kwargs):
        context = super(ResumeList, self).get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        return context

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.pk)

    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))


class ApplicantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    success_url = reverse_lazy('applicant:view')
    form_class = ApplicantEditForm
    title = 'Редактировать данные профиля'
    template_name = 'applicantapp/applicant_form.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main_list'))
