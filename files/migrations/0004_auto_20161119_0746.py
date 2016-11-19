# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 07:46
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('files', '0003_auto_20161018_1754'), ]

    operations = [
        migrations.AlterField(
            model_name='fynode',
            name='name',
            field=models.CharField(max_length=255), ),
        migrations.AlterField(
            model_name='inode',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now), ),
        migrations.AlterField(
            model_name='inode',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now), ),
    ]
