# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0009_auto_20180123_1135'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='postlist',
            new_name='PostModel',
        ),
    ]
