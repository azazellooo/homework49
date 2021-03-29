from django.views.generic import ListView, DetailView, CreateView

from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'project/view.html'
    model = Project


class ProjectCreateView(CreateView):
    pass