# Generated by Django 2.2.9 on 2020-02-01 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0004_auto_20200201_2247'),
        ('product', '0003_auto_20191221_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bom.Bom', verbose_name='Bom Name'),
        ),
    ]
