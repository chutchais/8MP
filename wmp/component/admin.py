from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Module,Component

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class ModuleResource(resources.ModelResource):
    class Meta:
        model = Module
        import_id_fields = ('number',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','registered_date','last_modified_date','slug' )


class ModuleAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['number','title','description','pn']
    list_filter = ['pn_type','category1','category2']
    list_display = ('number','pn','rev','title','parent','reserved_for','pn_type','registered_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','registered_date','last_modified_date')
    autocomplete_fields = ['parent','reserved_for']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['number','title',('pn','rev'),'description','category1','category2','status']}),
        ('Assembly Information',{'fields': ['parent','reserved_for']}),
        ('Property',{'fields': ['datecode','lotcode','supcode','pn_type']}),
        ('System Information',{'fields':[('user','registered_date'),'last_modified_date','slug']})
    ]
    resource_class      = ModuleResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ModuleAdmin, self).save_model(request, obj, form, change)

admin.site.register(Module,ModuleAdmin)


class ComponentResource(resources.ModelResource):
    class Meta:
        model = Component
        import_id_fields = ('number',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','registered_date','last_modified_date','slug' )

class ComponentAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['number','title','description','pn']
    list_filter = ['carrier','category1','category2','msl']
    list_display = ('number','barcode','pn','rev','title','qty','carrier','registered_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','registered_date','last_modified_date')
    autocomplete_fields = []
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['number','barcode',('pn','rev'),'title',
        						'description','category1','category2','status']}),
        ('Property',{'fields': ['datecode','lotcode','supcode','carrier','qty']}),
        ('MSD Information',{'fields': ['msl','met',('floor_life','shelf_life'),
        								'exp_date',('baking_start_date','baking_finish_date')]}),
        ('System Information',{'fields':[('user','registered_date'),'last_modified_date','slug']})
    ]
    resource_class      = ComponentResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ComponentAdmin, self).save_model(request, obj, form, change)

admin.site.register(Component,ComponentAdmin)