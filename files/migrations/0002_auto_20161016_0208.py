# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-16 02:08
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inode',
            fields=[
                ('fynode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                    parent_link=True, primary_key=True, serialize=False, to='files.FYNode')),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('size', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('tree_id', 'lft'),
                'abstract': False,
            },
            bases=('files.fynode',),
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('inode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                                                   parent_link=True, primary_key=True, serialize=False, to='files.Inode')),
                ('path', models.FilePathField(allow_files=False, allow_folders=True,
                                              path='/Users/pellaeon/project/fengyuan/data/', recursive=True)),
            ],
            options={
                'ordering': ('tree_id', 'lft'),
                'abstract': False,
            },
            bases=('files.inode',),
        ),
        migrations.AddField(
            model_name='inode',
            name='owner',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
