# coding:utf-8

from django.conf.urls import patterns, include, url
from views import *
from django.views.generic import RedirectView


urlpatterns = patterns('',
                       url(r'^$',RedirectView.as_view(url='/')),
                       )