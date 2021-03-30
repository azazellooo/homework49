from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import reverse

from webapp.models import Project
from webapp.forms import ProjectForm


class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'project/view.html'
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url = '/projects'


class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.kwargs.get('pk')})