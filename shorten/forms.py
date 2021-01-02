from django import forms
from django.forms.forms import Form
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
    url_validate = URLValidator()
    try:
        v1 =  url_validate(value)
    except:
        try:
                v2 =  url_validate('http://'+value)
        except:
            raise ValidationError("Invalid URL for this field")


class ShortenURLForm(forms.Form):
    url = forms.CharField(label = '' , validators=[validate_url],widget=forms.TextInput(attrs={'class' : 'form-control'}))

    def clean_url(self):
        data = self.cleaned_data['url']
        if "http://" not in data:
            data = "http://"+ data
        return data
    