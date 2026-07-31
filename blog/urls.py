from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path('', views.start_page , name='start_page'),
    path('<int:pk>/<slug>', views.detail_page, name="detail_page"),
    path('podcasts/<int:pk>/<slug>/', views.PodcastDetailView.as_view(), name="podcast_detail"),
    path('posts/', views.PostListView.as_view(), name="post_list"),
    path('podcasts/', views.PodcastListView.as_view(), name="podcast_list"),
]