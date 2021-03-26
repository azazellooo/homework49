from django.contrib import admin

from webapp.models import Issue, Type, Status, Project


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at', 'project']
    list_filter = ['created_at', 'status', 'type']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary']
    list_filter = ['started_at']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'started_at', 'finished_at']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)

# Register your models here.


