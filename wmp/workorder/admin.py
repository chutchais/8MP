from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import WorkOrder


from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class WorkOrderResource(resources.ModelResource):
    class Meta:
        model = WorkOrder
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        # fields = ('name', 'title', 'pn', 'rev', 'routing', 'regexp', 'description', 
        #             'category1', 'category2', 'fg_pn', 'fg_rev', 'parent', 'status')
        exclude = ('user','created_date','modified_date','slug' )

class WorkOrderAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['product','category1','category2']
    list_display = ('name','title','product','routing','regexp','qty','build_type','registered','category1','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    autocomplete_fields = ['product','routing']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','qty','build_type','description','category1','category2']}),
        ('Serial Number Format Control',{'fields': ['regexp']}),
        ('Routing Control',{'fields': ['routing']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = WorkOrderResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(WorkOrderAdmin, self).save_model(request, obj, form, change)
admin.site.register(WorkOrder,WorkOrderAdmin)