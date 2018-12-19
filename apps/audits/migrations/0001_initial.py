# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FTPLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=128, verbose_name='User')),
                ('remote_addr', models.CharField(blank=True, max_length=15, null=True, verbose_name='Remote addr')),
                ('asset', models.CharField(max_length=1024, verbose_name='Asset')),
                ('system_user', models.CharField(max_length=128, verbose_name='System user')),
                ('operate', models.CharField(max_length=16, verbose_name='Operate')),
                ('filename', models.CharField(max_length=1024, verbose_name='Filename')),
                ('is_success', models.BooleanField(default=True, verbose_name='Success')),
                ('date_start', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]