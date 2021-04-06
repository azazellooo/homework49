from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.db.models import Q
from django.utils.http import urlencode


from todolist.models import Issue, Project
from todolist.forms import IssueForm, SearchForm


class IssueListView(ListView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 10
    paginate_orphans = 3
    ordering = '-created_at'

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        return queryset

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self):
        context = super().get_context_data()
        context['search_form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search_value': self.search_value})
        return context


class IssueView(TemplateView):
    template_name = 'issue/view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['issue'] = issue
        return context


class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue/create.html'
    form_class = IssueForm

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class IssueUpdateView(UpdateView):
    model = Issue
    template_name = 'issue/update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue-view', kwargs={'pk': self.kwargs.get('pk')})


class IssueDeleteView(DeleteView):
    template_name = 'issue/delete.html'
    model = Issue
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.project.pk})


# Create your views here.
