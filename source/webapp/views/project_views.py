from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User

from webapp.models import Project
from webapp.forms import ProjectForm, ProjectUserForm


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


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project'
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_project'
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.kwargs.get('pk')})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False)


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_project'
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


# class ProjectUsersAdd(LoginRequiredMixin, TemplateView):
#     template_name = 'project/users_update.html'
#
#     def get_context_data(self, **kwargs):
#         users = User.objects.all()
#         project = get_object_or_404(Project, pk=kwargs.get('pk'))
#         context = super().get_context_data(**kwargs)
#         context['users'] = users
#         context['project'] = project
#         return context
#
#     def post(self, request, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs.get('pk'))
#         adding_user = request.POST.getlist('user')
#         print(project.user.all())
#         print(adding_user)
#         project.user.add(adding_user)
#         return reverse('project-view', kwargs={'pk':self.kwargs.get('pk')})

class ProjectUsersUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.can_update_project_user'
    model = Project
    template_name = 'project/users_update.html'
    form_class = ProjectUserForm

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        users = project.user.all()
        return super().has_permission() and self.request.user in users

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.kwargs.get('pk')})