# -*- coding: utf-8 -*-
"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/

Do not include views from other apps directly, use include()!
"""
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^blog/', include('blog.urls')),
]
