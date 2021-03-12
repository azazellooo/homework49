from django.contrib import admin

from webapp.models import Issue, Type, Status


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at']
    list_filter = ['created_at', 'status', 'type']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Type)
admin.site.register(Status)
# Register your models here.


