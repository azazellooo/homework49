from django.urls import path

from webapp.views.issue_views import IssueView, IssueCreateView, IssueDeleteView, IssueUpdateView
from webapp.views.project_views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectUsersUpdate
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-view'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('project/add', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project-delete'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue-view'),
    path('project/<int:pk>/users/update', ProjectUsersUpdate.as_view(), name='user-add'),
    path('<int:pk>/issue/add/', IssueCreateView.as_view(), name='issue-create'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue-delete'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
]