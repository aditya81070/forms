# Generated by Django 2.0.4 on 2018-04-21 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0015_auto_20180415_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort',
            name='sortchoices',
            field=models.CharField(choices=[('usernameatoz', 'By username A-Z'), ('usernameztoa', 'By username Z-A'), ('emailatoz', 'By Email A-Z'), ('emailztoa', 'By Email Z-A')], default=('usernameatoz', 'By username A-Z'), max_length=10),
        ),
    ]
