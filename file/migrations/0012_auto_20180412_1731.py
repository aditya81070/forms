# Generated by Django 2.0.4 on 2018-04-12 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0011_auto_20180202_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sortchoices', models.CharField(choices=[('Name', 'NAME'), ('Email', 'EMAIL')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='year',
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='username',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 8', regex='^.{8}')]),
        ),
    ]
