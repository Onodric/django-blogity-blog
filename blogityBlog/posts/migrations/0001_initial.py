# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models
import posts.models.posts


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('subheading', models.CharField(max_length=180)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=posts.models.posts.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', markdownx.models.MarkdownxField()),
                ('location', models.CharField(max_length=30)),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default='bdmarks4', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='posts.Category')),
            ],
            options={
                'verbose_name_plural': 'posts',
            },
        ),
    ]
