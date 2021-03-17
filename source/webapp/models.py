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
    created_at = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

# Create your models here.
