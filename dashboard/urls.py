from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.user_area, name='userarea'),
    path('update_user/', views.validate_and_save_user_informations, name='updateuser'),
]