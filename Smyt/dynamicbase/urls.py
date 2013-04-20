# coding:utf-8

from django.conf.urls import patterns, include, url
from views import *
from django.views.generic import RedirectView


urlpatterns = patterns('',
                       url(r'^data.json',Table.as_view(),name='json_table'),
                       url(r'^(?P<table>.+).json',Table.as_view(),name='json_table'),

                       url(r'^(?P<table>.+).form',RowForm.as_view(),name='edit'),
                       url(r'^form',RowForm.as_view(),name='edit'),

                       url(r'^$',Home.as_view(),name='home'),
                       url(r'^(?P<table>.+).html$',Home.as_view(),name='home'),
                       )