
import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже используется.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Этот логин уже используется.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise ValidationError("Пароль должен содержать минимум 8 символов.")

        if not re.search(r'[A-Z]', password):
            raise ValidationError("Пароль должен содержать хотя бы одну заглавную букву.")

        if not re.search(r'[a-z]', password):
            raise ValidationError("Пароль должен содержать хотя бы одну строчную букву.")

        if not re.search(r'[0-9]', password):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Пароль должен содержать хотя бы один специальный символ.")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
