from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/
    path('', views.register, name='register'),
    # ex: /accounts/login
    path('login/', views.login, name='login'),
    # ex: /accounts/logout
    path('logout/', auth_views.LogoutView.as_view(template_name='computers/home.html',
                                                  next_page='/'),
         name='logout'),
]
