# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='read_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
