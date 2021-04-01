from django import forms
from django.forms.fields import BooleanField

from vacancyapp.models import Vacancy


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ('is_active', 'company', 'is_approved', 'is_approved',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
