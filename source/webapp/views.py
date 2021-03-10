from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView

from webapp.models import Issue
from webapp.forms import IssueForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = Issue.objects.all()
        context['issues'] = issues
        return context


class IssueView(TemplateView):
    template_name = 'issue_view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['issue'] = issue
        return context


class IssueCreateView(View):
    pass
# Create your views here.
