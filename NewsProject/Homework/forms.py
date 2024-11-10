from django import forms
from django.template.defaultfilters import title

from .models import Profession, Human
import re
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class HumanForm(forms.ModelForm):
    captcha = CaptchaField()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.search('максим', first_name.lower()):
            raise ValidationError(
                'Имя "Максим" забронировано и Вы не можете им распоряжаться')
        return first_name

    class Meta:
        model = Human
        # fields = '__all__'
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'biography',
            'date_of_birth',
            'is_adult',
            'profession',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'biography': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'date_of_birth': forms.SelectDateWidget(attrs={
                'class': 'form-control',
            }),
            'profession': forms.Select(attrs={
                'class': 'form-control',
            }),
        }