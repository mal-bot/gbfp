from django import forms

from authapp.models import User
from django.forms.fields import BooleanField


class ApplicantEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'user_patronymic', 'email', 'user_about', 'user_age', 'file')

    def __init__(self, *args, **kwargs):
        super(ApplicantEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
