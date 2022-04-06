"""systemCodeManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.firstpage, name = 'firstpage'),
    path('History', views.showhistory, name = 'showhistory'),
    path('Insert', views.insertrecord, name = 'insertrecord'),
    path('Insert_Record', views.insert_record, name = 'insert_record'),
    path('Display', views.display, name = 'display'),
  
    path('Delete/<int:currentweek>', views.delete, name = "delete"),
    path('Delete_sys/<int:id>/<str:empname>/<int:currentweek>', views.delete_sys, name = "delete_sys"),
     path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path('read_file', views.read_file, name = 'read_file'),

]
