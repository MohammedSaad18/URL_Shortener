from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(    
            Row(
                Column('username', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password2', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Sign up', css_class='form-group col-md-12 mb-0')
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']