from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.index, name='code_editor_landing_page'),
    path('python', views.python_editor, name='python_editor'),
    path('python/save_data/', views.save_data, name='save_data'),
]
