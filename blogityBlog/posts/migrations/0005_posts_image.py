# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170731_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]