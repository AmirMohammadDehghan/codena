"""
URL configuration for academycodna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

# from django_otp.admin import OTPAdminSite
#
# admin.site.__class__ = OTPAdminSite

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('196810.txt', RedirectView.as_view(url=staticfiles_storage.url('196810.txt'))),
    path('422680.txt', RedirectView.as_view(url=staticfiles_storage.url('422680.txt'))),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),

    path('academycodena/admin/', admin.site.urls),
    path('', include('django_sso.sso_gateway.urls')),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('users.urls')),
    path('', include('cart.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ATM/', include('ATM.urls')),
    path('editor/', include('editor.urls')),
    path('roadmap-<roadmap_id>/', include('roadmap.urls')),
    path('members/', include('MembersDietail.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from simple_sso.sso_server.server import Server
# my_server = Server()
# urlpatterns += [
#     path('server/', include(my_server.get_urls())),
# ]
