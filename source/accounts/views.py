from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from accounts.forms import UserRegisterForm
from django.contrib.auth.mixins import PermissionRequiredMixin

from accounts.models import Profile


def register_view(request, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('project-list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        projects = self.object.project.all()
        kwargs['projects'] = projects
        return super().get_context_data(**kwargs)


class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'accounts.can_view_user_list'
    template_name = 'user_list.html'
    model = get_user_model()
    context_object_name = 'users'
# Create your views here.
