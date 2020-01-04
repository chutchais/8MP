from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import SerialNumber

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class SerialNumberResource(resources.ModelResource):
    class Meta:
        model = SerialNumber
        import_id_fields = ('number','workorder')
        skip_unchanged = True
        report_skipped= True
        # fields = ('name', 'title', 'pn', 'rev', 'routing', 'regexp', 'description', 
        #             'category1', 'category2', 'fg_pn', 'fg_rev', 'parent', 'status')
        exclude = ('id','user','slug' )

class SerialNumberAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['number','workorder__name']
    list_filter = ['wip','current_operation','last_operation']
    list_display = ('number','workorder','current_operation','last_operation','last_modified_date','last_result','wip')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','parent','unit_type','last_modified_date')
    autocomplete_fields = ['workorder','routing']
    fieldsets = [
        ('Basic Information',{'fields': [('number','unit_type'),'workorder','routing',
            'description','category1','category2','wip','user']}),
        ('Assembly Imformation',{'fields': ['parent']}),
        ('Performing',{'fields': ['current_operation',('perform_operation','perform_resource','perform_start_date')]}),
        ('Last Performance',{'classes': ('collapse','wide', 'extrapretty'),
            'fields': [('last_operation','last_modified_date'),'last_result']}),
        ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SerialNumberAdmin, self).save_model(request, obj, form, change)
admin.site.register(SerialNumber,SerialNumberAdmin)