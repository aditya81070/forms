# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-23 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20180123_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlist',
            name='Email',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
    ]
