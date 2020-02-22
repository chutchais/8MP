from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

from .models import SymptomCode,SymptomCode_Usage


class SymptomCodeResource(resources.ModelResource):
    class Meta:
        model = SymptomCode
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug' )

class SymptomCodeUsageInline(admin.TabularInline):
    model = SymptomCode_Usage
    fields = ('ordered','routingdetail','title','status','modified_date')
    extra = 0 # how many rows to show
    autocomplete_fields = ['routingdetail']
    readonly_fields = ['modified_date']
    show_change_link = True
    verbose_name = 'Symptom Code Usage detail'
    verbose_name_plural = 'Symptom Code Usage detail'

class SymptomCodeAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    # filter_horizontal = ('products',)
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description',
                            'slug','category1','category2','user']}),
        # ('Assign to ',{'fields': ['products']}),
    ]
    resource_class      = SymptomCodeResource 
    inlines = [SymptomCodeUsageInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SymptomCodeAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(SymptomCode,SymptomCodeAdmin)