from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm


def register_view(request, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)

# Create your views here.
