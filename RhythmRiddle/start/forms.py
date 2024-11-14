
import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    country_choices = [
        ('RU', 'Россия'),
        ('KK', 'Казахстан'),
        # потом дополнить
    ]
    country = forms.ChoiceField(choices=country_choices)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'country', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже используется.")
        return email

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

    def generate_username(self, first_name, last_name):
        base_username = f"{first_name.lower()}_{last_name.lower()}"
        username = base_username
        counter = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        user.username = self.generate_username(first_name, last_name)

        if commit:
            user.save()
        return user
