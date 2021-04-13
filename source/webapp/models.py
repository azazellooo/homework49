from django.contrib.auth import get_user_model
from django.db import models
from webapp.validators import SymbolCheckValidator, ForbiddenWordsValidator


class Type(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'


class Status(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'


class Project(models.Model):
    started_at = models.DateField(verbose_name='Дата начала')
    finished_at = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    summary = models.CharField(max_length=130, verbose_name='Название')
    description = models.TextField(max_length=5000, verbose_name='Описание')
    is_deleted = models.BooleanField(default=False)
    user = models.ManyToManyField(get_user_model(), related_name='user', verbose_name='Пользователи')


class Issue(models.Model):
    summary = models.CharField(max_length=130,
                               null=False,
                               blank=False,
                               verbose_name='Название',
                               validators=[SymbolCheckValidator(["%", "$", "@", "#", "^", "&"]), ]
                               )
    description = models.TextField(max_length=3000,
                                   null=False,
                                   blank=True,
                                   verbose_name='Описание',
                                   validators=[ForbiddenWordsValidator(['наркотики', 'насилие', 'алкоголь', 'терроризм']), ]
                                   )
    type = models.ManyToManyField('webapp.Type', related_name='type', verbose_name='Тип')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    project = models.ForeignKey('webapp.Project', related_name='issue', on_delete=models.CASCADE, verbose_name='Из проекта')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')


# Create your models here.
