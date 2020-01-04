# Generated by Django 2.0.4 on 2018-07-16 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workorder', '0001_initial'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('category1', models.CharField(blank=True, max_length=50, null=True)),
                ('category2', models.CharField(blank=True, max_length=50, null=True)),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(blank=True, null=True)),
                ('last_result', models.BooleanField(default=False, verbose_name='Last Result')),
                ('finished_date', models.DateTimeField(blank=True, null=True)),
                ('wip', models.BooleanField(default=True, verbose_name='Work In Process')),
                ('perform_start_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactive')], default='A', max_length=1)),
                ('current_operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currentoperation', to='operation.Operation')),
                ('last_operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lastoperation', to='operation.Operation')),
                ('perform_operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performoperation', to='operation.Operation')),
                ('routing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='routing.Routing')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('workorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorder.WorkOrder')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='serialnumber',
            unique_together={('number', 'workorder')},
        ),
    ]
