# Generated by Django 2.0.4 on 2018-07-16 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternate_Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pn', models.CharField(max_length=50, verbose_name='Part Number')),
                ('customer_pn', models.CharField(blank=True, max_length=50, null=True)),
                ('ordered', models.IntegerField(default=1)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bom',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pn', models.CharField(blank=True, max_length=50, null=True, verbose_name='Part Number')),
                ('rev', models.CharField(blank=True, max_length=10, null=True, verbose_name='Revision')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('customer_pn', models.CharField(blank=True, max_length=50, null=True, verbose_name='Customer Part Number')),
                ('customer_rev', models.CharField(blank=True, max_length=10, null=True, verbose_name='Customer Revision')),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bom_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rd', models.CharField(max_length=50, verbose_name='Ref Destinator')),
                ('pn', models.CharField(max_length=50, verbose_name='Part Number')),
                ('customer_pn', models.CharField(blank=True, max_length=50, null=True, verbose_name='Customer Part Number')),
                ('pn_type', models.CharField(choices=[('COMPONENT', 'Component'), ('MODULE', 'Module with serial number')], default='COMPONENT', max_length=10, verbose_name='Part Type')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('bom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bom.Bom')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alternate_part',
            name='bom_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternates', to='bom.Bom_Detail'),
        ),
        migrations.AddField(
            model_name='alternate_part',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='bom_detail',
            unique_together={('rd', 'pn', 'bom')},
        ),
    ]
