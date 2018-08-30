# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from . import *


class UserRole(models.Model):
    user = models.OneToOneField(User, related_name='client_admin_role', on_delete=models.CASCADE)
    ### role == 1 for admin
    ### role == 2 for client
    role = models.IntegerField(default=0)
    is_removed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username


class Rack(models.Model):
    name = models.CharField(max_length=512,default='')
    book_count = models.IntegerField(default=0)
    is_removed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=512,default='')
    author_name = models.CharField(max_length=512,default='')
    publish_year = models.CharField(max_length=32,default='0000')
    is_removed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class RackBook(models.Model):
    book = models.OneToOneField(Book, related_name='book_object', on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, related_name='rack_object', on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)

