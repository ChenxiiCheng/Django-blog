# _*_ coding: utf-8 _*_
__author__ = 'chenxi'
__date__ = '2/27/19 5:55 PM'

from django import template
from ..models import Post, Category


register = template.Library()


# 自定义模板标签，直接在模板中可以用，就不需要再view里获取数据库的数据，再传给前端
# 通过自定义模板标签前端可以直接获取数据库里的数据
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()
