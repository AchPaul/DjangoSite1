from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import *


class AddPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):#Для непустого поля выбора
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:#связка с моделью БД
        model = Women
        fields = '__all__'

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-input'})
    }

    def clean_title(self):#валидатор
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина больше 200')
        return title


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин: ', widget=forms.TextInput(attrs={'class': ' '}))
    email = forms.EmailField(label='Email: ', widget=forms.EmailInput(attrs={'class': ' '}))
    password1 = forms.CharField(label='Пароль: ', widget=forms.PasswordInput(attrs={'class': ' '}))
    password2 = forms.CharField(label='Подтвердите пароль: ', widget=forms.PasswordInput(attrs={'class': ' '}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин: ', widget=forms.TextInput(attrs={'class': ' '}))
    password = forms.CharField(label='Пароль: ', widget=forms.PasswordInput(attrs={'class': ' '}))


class ContactFormView(forms.Form):
    name = forms.CharField(label='Имя: ', max_length=50)
    email = forms.EmailField(label='Email: ')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Сообщение: ', max_length=255)
    captcha = CaptchaField()