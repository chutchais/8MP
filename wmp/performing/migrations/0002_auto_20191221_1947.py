# Generated by Django 2.2.9 on 2019-12-21 12:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('performing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performing',
            name='loop',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='performing',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
