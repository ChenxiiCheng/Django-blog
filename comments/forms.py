# _*_ coding: utf-8 _*_
__author__ = 'chenxi'
__date__ = '2/27/19 8:44 PM'

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']


