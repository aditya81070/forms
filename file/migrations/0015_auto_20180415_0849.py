# Generated by Django 2.0.4 on 2018-04-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0014_auto_20180415_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort',
            name='sortchoices',
            field=models.CharField(choices=[('username', 'By username A-Z'), ('-username', 'By username Z-A'), ('Email', 'By Email A-Z'), ('-Email', 'By Email Z-A')], default=('username', 'By username A-Z'), max_length=10),
        ),
    ]
