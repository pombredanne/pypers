# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_authors', models.CharField(max_length=512, verbose_name='authors')),
                ('authors', models.CharField(max_length=128, verbose_name='authors')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='year')),
                ('citekey', models.CharField(max_length=16, unique=True, verbose_name='citekey')),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='rating')),
                ('notes', models.TextField(null=True, verbose_name='notes')),
                ('summary', models.TextField(null=True, verbose_name='summary')),
                ('annotations', models.TextField(null=True, verbose_name='annotations')),
                ('read_status', models.BooleanField(verbose_name='read_status')),
                ('imported_date', models.DateField(blank=True, null=True, verbose_name='imported_date')),
                ('pdf_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='pdf_path')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='tags',
            field=models.ManyToManyField(to='papers.Tag'),
        ),
    ]
