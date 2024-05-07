
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class EditarPacientesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email