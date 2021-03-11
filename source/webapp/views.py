from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
    form = IssueForm
    template_name = 'issue_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(data=request.POST)

        if form.is_valid():
            Issue.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                type=form.cleaned_data.get('type'),
                status=form.cleaned_data.get('status')
            )
            return redirect('issue-list')
        return render(request, self.template_name, {'form': form})


class IssueDelete(View):
    template_name = 'issue_delete.html'

    def get(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return render(request, self.template_name, {'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        issue.delete()
        return redirect('issue-list')

# Create your views here.
