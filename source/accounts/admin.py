from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Profile
from django.contrib.auth import get_user_model


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['avatar', 'github', 'about_user']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


User = get_user_model()
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
# Register your models here.
