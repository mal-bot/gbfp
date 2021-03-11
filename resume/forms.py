from django import forms
from django.forms.fields import BooleanField

from resume.models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super(ResumeEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
