from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account'
urlpatterns = [
    
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('forget-password/', ForgetPassword, name='forget_password'),
    path('change-password/<token>/', ChangePassword, name='change_password'),
    path('logout/', Logout, name='logout'),
    path('userslist/', UsersListView.as_view(), name='users-list'),
    path('export-users-excel/', export_users_excel, name='export_users_excel'),
]

