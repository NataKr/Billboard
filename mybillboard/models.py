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
        return self.user_name

    def get_date(self):
        return self.post_date.date()
    def get_day(self):
        return self.post_date.day
    def get_month(self):
        return self.post_date.month
    def get_year(self):
        return self.post_date.year