from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        help_text='Максимум 150 символов',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    password1 = forms.CharField(
        label='Пароль',
        # help_text='Максимум 150 символов',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        # help_text='Максимум 150 символов',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )
    email = forms.EmailField(
        label = 'Электронная почта',
        # help_text='Максимум 150 символов',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }),
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #     }),
        # }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        # help_text='Максимум 150 символов',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    password = forms.CharField(
        label='Пароль',
        # help_text='Максимум 150 символов',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )