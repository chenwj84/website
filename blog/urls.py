# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.archive),
    url(r'^create/', views.create_blogpost),
    url(r'^sendmail/', views.send_view_email),
]