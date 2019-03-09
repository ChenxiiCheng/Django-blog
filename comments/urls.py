# _*_ coding: utf-8 _*_
__author__ = 'chenxi'
__date__ = '2/27/19 9:02 PM'


from django.conf.urls import url

from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
