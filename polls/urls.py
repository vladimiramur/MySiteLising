from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.operation_new, name='operation_new'),

)
