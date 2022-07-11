from django.urls import path

from . import views

app_name = 'computers'
urlpatterns = [
    # ex: /
    path('', views.home, name='home'),
    # ex: /computers/id
    path('computers/<int:computer_id>/', views.detail, name='detail'),
]
