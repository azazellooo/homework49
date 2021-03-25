from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView
from django.db.models import Q
from django.utils.http import urlencode


from webapp.models import Issue
from webapp.forms import IssueForm, SearchForm


class IssueListView(ListView):
    template_name = 'index.html'
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
            issue = Issue.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status')
            )
            issue_type = form.cleaned_data.pop('type')
            issue.type.set(issue_type)
            return redirect('issue-list')
        return render(request, self.template_name, {'form': form})


class IssueUpdate(View):
    template_name = 'issue_update.html'

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(initial={
            'summary': issue.summary,
            'description': issue.description,
            'type': issue.type.all(),
            'status': issue.status
        })

        return render(request, self.template_name, context={'issue': issue, 'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        if form.is_valid():
            issue_type = form.cleaned_data.pop('type')
            issue.type.set(issue_type)
            issue.summary = form.cleaned_data.get('summary')
            issue.description = form.cleaned_data.get('description')
            issue.status = form.cleaned_data.get('status')

            issue.save()
            return redirect('issue-list')
        return render(request, self.template_name, context={'issue': issue, 'form': form})


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
