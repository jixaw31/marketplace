from django.urls import path, include
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('log-in/', views.log_in, name='log-in'),
    path('log-out/', views.log_out, name='log-out'),
    path('add-item/', views.addItem, name='add-item'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
]
