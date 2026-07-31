from django.urls import path
from . import views

urlpatterns = [
    path('request/<price>', views.send_request, name='request'),
    path('request/course/<cors_id>/<discount_code>', views.course_payment_request, name='course_request'),
    path('request/faze/<faz_id>/<discount_code>', views.faze_payment_request, name='faze_request'),
    path('verify/', views.verify , name='verify'),
    path('verify/<cors_id>/<discount_code>/', views.course_payment_verify, name='course_verify'),
    path('verify/faze/<faz_id>/<discount_code>/', views.faze_payment_verify, name='faze_verify'),
    path('verified', views.verified, name='verified'),
    path('process-payment/', views.process_payment_view, name='process_payment'),
    path('callback/', views.callback_view, name='callback'),
]