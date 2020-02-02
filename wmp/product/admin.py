from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Product

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        fields = ('name', 'title', 'pn', 'rev', 'routing', 'regexp', 'description', 
                    'category1', 'category2', 'fg_pn', 'fg_rev', 'parent', 'status','bom')
        # exclude = ('user','created_date','modified_date','slug' )


class ProductAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','pn','fg_pn']
    list_filter = ['category1','category2']
    list_display = ('name','title','pn','rev','routing','regexp','category1','parent','bom','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    autocomplete_fields = ['parent','routing','bom']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title',('pn','rev'),'description','category1','category2','status']}),
        ('Parent Product',{'fields': ['parent']}),
        ('BOM',{'fields': ['bom']}),
        ('Serial Number Format Control',{'fields': ['regexp']}),
        ('Routing Control',{'fields': ['routing']}),
        ('Finish Goods Information',{'fields': ['fg_pn','fg_rev']}),  
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = ProductResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)

admin.site.register(Product,ProductAdmin)