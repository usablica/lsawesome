from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Category(models.Model):
    # meta data
    creation_datetime = models.DateTimeField('creation date', default=timezone.now())
    update_datetime = models.DateTimeField('last update', default=timezone.now())
    # fields
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True)


class List(models.Model):
    # meta data
    creation_datetime = models.DateTimeField('creation date', default=timezone.now())
    update_datetime = models.DateTimeField('last update', default=timezone.now())
    # fields
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    github = models.URLField()


class Item(models.Model):
    # meta data
    creation_datetime = models.DateTimeField('creation date', default=timezone.now())
    update_datetime = models.DateTimeField('last update', default=timezone.now())
    # fields
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    ls = models.ForeignKey(List)
    github = models.URLField()
