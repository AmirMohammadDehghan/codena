from django.urls import path
from . import views

app_name = 'roadmaps'

urlpatterns = [
    path("", views.RoadMapListView.as_view(), name="RoadMapListView"),
]
