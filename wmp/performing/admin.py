from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from performing.models import Performing

class PerformingAdmin(admin.ModelAdmin):
    search_fields = ['sn__number']
    list_filter = ['operation','resource_name']
    list_display = ('sn','operation','result','interval','resource_name','start_time','stop_time','duration')
    # list_editable = ('color','move_performa')
    readonly_fields = ('uid','created_date','user')
    autocomplete_fields = []
    # save_as = True
    # save_as_continue = True
    # save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['sn','result']}),
        ('Transaction Information',{'fields': ['operation','interval',
        		'resource_name',('start_time','stop_time'),'remark']}),
        ('System Information',{'fields':[('user','created_date')]})
        # 'perform_year','perform_month','perform_day','perform_hour'
    ]
    # resource_class      = ProductResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(PerformingAdmin, self).save_model(request, obj, form, change)

admin.site.register(Performing,PerformingAdmin)