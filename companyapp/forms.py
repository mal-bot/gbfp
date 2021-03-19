from django import forms

from authapp.models import User
from django.forms.fields import BooleanField


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('company_name', 'company_main_business', 'email', 'company_about', 'company_since', 'file')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
