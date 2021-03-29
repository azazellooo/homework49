from django.views.generic import ListView, DetailView, CreateView

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
