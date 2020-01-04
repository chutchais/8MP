from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Operation

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


class OperationResource(resources.ModelResource):
    class Meta:
        model = Operation
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug' )

class OperationAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2','customer_name']
    list_filter = ['category1','category2','customer_name']
    list_display = ('name','title','customer_name','operation_type','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
        ('Operation Type',{'fields': ['operation_type']}),
        ('Customer Information',{'fields': ['customer_name']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = OperationResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(OperationAdmin, self).save_model(request, obj, form, change)

admin.site.register(Operation,OperationAdmin)


