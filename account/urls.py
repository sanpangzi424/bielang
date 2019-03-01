"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('my-information/', views.myself, name='my_information'),
    path('edit-my-information/', views.myself_edit, name='edit_my_information'),
    path('logout/', auth_views.logout, {'template_name':'account/logout.html'}, name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.password_change, {'post_change_redirect':'/account/password-change-done/'}, name='password_change'),
    path('password-change-done/', auth_views.password_change_done, name='password_change_done'),

]
