from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse

from webapp.models import Project
from webapp.forms import ProjectForm


class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


class ProjectDetailView(DetailView):
    template_name = 'project/view.html'
    model = Project

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')


class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.kwargs.get('pk')})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project-list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)