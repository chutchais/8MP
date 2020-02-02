# Generated by Django 2.2.9 on 2020-02-01 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_auto_20191221_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name does not allow special charecters', regex='^[\\w-]+$')]),
        ),
    ]
