from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ApplicantRegistrationForm(UserCreationForm):
    pass


class CompanyRegistrationForm(UserCreationForm):
    pass
