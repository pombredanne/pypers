from django.db import models


class Label(models.Model):
    name = models.CharField('name', max_length=128)


class Paper(models.Model):
    authors = models.CharField('authors', max_length=256)
    title = models.CharField('title', max_length=256)
    year = models.PositiveSmallIntegerField('year', blank=True, null=True)
    mark = models.PositiveSmallIntegerField('mark', blank=True, null=True)
    notes = models.TextField('notes')
    labels = models.ManyToManyField(Label)
