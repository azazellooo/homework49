from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView
from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_object_name = 'user_object'
    form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()
        profile_form = self.get_profile_form()

        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)
        return self.form_invalid(user_form, profile_form)

    def form_valid(self, user_form, profile_form):
        response = super(UserUpdateView, self).form_valid(user_form)
        profile_form.save()
        return response

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(user_form=user_form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        return self.request.user

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return self.profile_form_class(**form_kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['profile_form'] = kwargs.get('profile_form')
        if context['profile_form'] is None:
            context['profile_form'] = self.get_profile_form()
        return context

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': self.object.pk})
