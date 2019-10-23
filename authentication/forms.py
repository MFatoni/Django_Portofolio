from django import forms

class Authentication_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan email',
    }
    attrs_user = {
        'placeholder' : 'Username',
        'class': 'form-control mb-3'
    }
    attrs_pass = {
        'placeholder' : 'Password',
        'class': 'form-control'
    }
    username = forms.CharField(label=False,required=True, max_length=27, widget=forms.TextInput(attrs=attrs_user))
    password = forms.CharField(label=False,required=True, widget=forms.PasswordInput(attrs=attrs_pass))