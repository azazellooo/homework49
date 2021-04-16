from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    github = models.URLField(null=True, blank=True, max_length=250, verbose_name='Ссылка на github')
    about_user = models.TextField(null=True, blank=True, verbose_name='О себе', max_length=3000)
# Create your models here.
