from django import forms

from Vacancy.models import Vacancy


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
