# Generated by Django 2.0.4 on 2018-12-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0007_auto_20181218_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptom',
            name='ndf',
        ),
        migrations.AddField(
            model_name='symptom',
            name='cnd',
            field=models.BooleanField(default=False, verbose_name='Can Not Duplicate'),
        ),
    ]
