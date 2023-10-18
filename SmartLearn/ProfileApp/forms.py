from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from CabinetApp.models import Cabinet
from ProfileApp.models import User, EmailVerification, Service
from django.utils.timezone import now
import uuid
from datetime import timedelta


class UserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_teacher = forms.BooleanField(label='Преподаватель', widget=forms.CheckboxInput(attrs={'class': 'form-check'}),
                                    required=False)
    images = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number',
                  'is_teacher', 'images']

    # def save(self, commit=True):
    #     user = super(UserRegisterForm, self).save(commit=True)
    #     expirations = now() + timedelta(hours=48)
    #     record = EmailVerification.objects.create(
    #         code=uuid.uuid4(),
    #         user=user,
    #         expirations=expirations,
    #     )
    #     record.send_verifications_email()
    #     return user


class CabinetForm(forms.ModelForm):
    class Meta:
        model = Cabinet
        fields = '__all__'


class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))
    images = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    is_published = forms.BooleanField(label='Опубликовано', widget=forms.CheckboxInput(attrs={'class': 'form-check'}),
                                    required=False)
    is_pinned = forms.BooleanField(label='Закреплено', widget=forms.CheckboxInput(attrs={'class': 'form-check'}),
                                    required=False)
    is_private = forms.BooleanField(label='Приватно', widget=forms.CheckboxInput(attrs={'class': 'form-check'}),
                                    required=False)

    class Meta:
        model = User
        fields = ['title', 'content', 'images', 'is_published', 'is_pinned', 'is_private']


class ServiceForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='Цена', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Service
        fields = ('name', 'description', 'price')