"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^new/$', views.new, name="my_new"),
    url(r'^(?P<id>\d+)/$', views.show, name="my_show"),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name="my_edit"),
    url(r'^create/$', views.create, name="my_create"),
    url(r'^(?P<id>\d+)/destroy/$', views.destroy, name="my_destroy"),
    url(r'^update/$', views.update, name="my_update"),
]

