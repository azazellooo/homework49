
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view, UserDetailView, UserListView, UserUpdateView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('userlist/', UserListView.as_view(), name='user_list'),
    path('update/', UserUpdateView.as_view(), name='user-update'),
    path('change-password/', UserPasswordChangeView.as_view(), name='change-password')
]