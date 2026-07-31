from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [

    path('', views.index, name='index'),
    # path('courses/<int:pk>/<slug>', views.course_detail, name="course_detail"),
    path('courses/<int:pk>/<slug>', views.CourseDetailView.as_view(), name="course_detail"),
    path('courses/create-ticket/<int:pk>/', views.CreateTicketView.as_view(), name="create_ticket_view"),
    path('courses/upload-ticket-media/', views.upload_ticket_media, name="upload_ticket_media"),
    path('temporary_discount_code/dvjhfdsj56fhosdar984dfd98we94/course_form/', views.temporary_discount_code_form_view,
         name='course_buy_form'),
    path('temporary_discount_code/knbvfdsj5g6fhosd3949348fd894k94/faze_form/',
         views.temporary_discount_code_form_faze_view, name='faze_buy_form'),
    path('contact-us', views.contact_us, name='contact'),
    path('about-us', views.about_us, name='about'),
    path('courses/', views.CourseListView.as_view(), name='CourseListView'),

]
