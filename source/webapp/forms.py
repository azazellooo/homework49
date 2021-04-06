from django import forms
from django.forms import widgets

from todolist.models import Type, Status, Issue, Project


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'type', 'status']


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Поиск')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['summary', 'description', 'started_at', 'finished_at']