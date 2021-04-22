from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError('Заполните одно из этих полей: first name или last name')
        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UserChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(required=True, label='Старый пароль', widget=PasswordInput)
    new_password = forms.CharField(required=True, label='Новый пароль', widget=PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подтверждение пароля', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password', 'password_confirm')

    def clean_password_confirm(self):
        new_password = self.cleaned_data.get('new_password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if new_password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return new_password

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')

        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Введите правильный старый пароль')

        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('new_password'))
        if commit:
            user.save()
        return user
