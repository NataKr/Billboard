# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
import datetime
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Post(models.Model):
    user_name=models.CharField(max_length=20)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=400)
    post_date=models.DateTimeField('post_date')

    def __str__(self):
        return self.subject

    def get_date(self):
        return self.post_date.date()
    def get_day(self):
        return self.post_date.day
    def get_month(self):
        return self.post_date.month
    def get_year(self):
        return self.post_date.year

@python_2_unicode_compatible
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date=models.DateTimeField('comment_date')
    comment_message=models.CharField(max_length=400)
    comment_user=models.CharField(max_length=20)

    def __str__(self):
        return self.post
    def get_date(self):
        return self.comment_date.date()
    def get_day(self):
        return self.comment_date.day
    def get_month(self):
        return self.comment_date.month
    def get_year(self):
        return self.comment_date.year

@python_2_unicode_compatible
class Comment_new(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date=models.DateTimeField('comment_date')
    comment_message=models.CharField(max_length=400)
    comment_user=models.CharField(max_length=20)

    def __str__(self):
        return unicode(self.post)
    def get_date(self):
        return self.comment_date.date()
    def get_day(self):
        return self.comment_date.day
    def get_month(self):
        return self.comment_date.month
    def get_year(self):
        return self.comment_date.year