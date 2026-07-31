from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart/', views.viewcartlist, name='cartlist'),
    path('delete-cartlist-item', views.deletecartlistitem,  name='deletecartitem'),
    path('add-to-cartlist', views.addtocart,  name='addtocartlist'), 


    path('add-faze-to-cartlist', views.addfazetocart, name='addfazetocart'),
    path('delete-faze-cartlist-item', views.deletefazecartlistitem,  name='deletecartfazeitem'),
]