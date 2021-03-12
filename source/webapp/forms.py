from django import forms
from django.forms import widgets

from webapp.models import Type, Status


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=130, required=True, label='Название')
    description = forms.CharField(max_length=3000, required=False, widget=widgets.Textarea, label='Подробнее о задаче')
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, label='Тип',
                                          widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус')

