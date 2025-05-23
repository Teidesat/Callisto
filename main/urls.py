"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import accounts.views
import shared.views
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts.views.user_login, name='login'),
    path('', shared.views.index, name='index'),
    path('logout/', accounts.views.user_logout, name='logout'),
    path('departments/', include('departments.urls')),
    path('user/leave/', users.views.leave, name='leave'),
    path('user/edit/', users.views.edit_profile, name='edit-profile'),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
