"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views.issue_views import IssueListView, IssueView, IssueCreateView, IssueDelete, IssueUpdate
from webapp.views.project_views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-view'),
    path('project/add', ProjectCreateView.as_view(), name='project-create'),
    path('', IssueListView.as_view(), name='issue-list'),
    path('<int:pk>/', IssueView.as_view(), name='issue-view'),
    path('issue/add/', IssueCreateView.as_view(), name='issue-create'),
    path('<int:pk>/delete', IssueDelete.as_view(), name='issue-delete'),
    path('<int:pk>/update/', IssueUpdate.as_view(), name='issue-update'),
]
