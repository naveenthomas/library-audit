"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from audit import views
from audit.views import ShelfList,ShelfCreate,ShelfUpdate,ShelfDelete

urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),
        
    # Shelf CRUD
    url(r'^shelf_list', ShelfList.as_view(),name = 'shelf-list'),
    url(r'^shelf_create', ShelfCreate.as_view(),name = 'shelf-create'),
    url(r'^shelf_update/(?P<pk>\d+)$', ShelfUpdate.as_view(),name = 'shelf-update'),
    url(r'^shelf_delete/(?P<pk>\d+)$', ShelfDelete.as_view(),name = 'shelf-delete')



]
