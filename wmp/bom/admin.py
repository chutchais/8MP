from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Bom
from .models import Bom_Detail
from .models import Alternate_Part

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class BomResource(resources.ModelResource):
    class Meta:
        model = Bom
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug' )


class BomDetailInline(admin.TabularInline):
    model = Bom_Detail
    fields = ['rd','pn','customer_pn','pn_type','title','critical']
    extra = 0
    show_change_link = True
    verbose_name = 'Bom detail'
    verbose_name_plural = 'Bom details'

class BomAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2','fg_pn']
    list_filter = ['category1','category2','status']
    list_display = ('name','title','pn','rev','items_count','category1','category2','status','user')
    readonly_fields = ('user','slug','created_date','modified_date')
    # autocomplete_fields = ['parent']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','pn','rev','description','category1','category2','status']}),
        ('Finish Goods Information',{'fields': ['fg_pn','fg_rev']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = BomResource
    inlines             = [BomDetailInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomAdmin, self).save_model(request, obj, form, change)

admin.site.register(Bom,BomAdmin)




class BomDetailResource(resources.ModelResource):
    class Meta:
        model = Bom_Detail
        import_id_fields = ('bom','rd','pn',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug','id' )

class AlternatePartInline(admin.TabularInline):
    model = Alternate_Part
    fields = ['ordered','pn','customer_pn','title']
    extra = 0
    verbose_name = 'Alternative Part'
    verbose_name_plural = 'Alternative Parts'

class BomDetailAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['rd','pn','bom__name','title','description','category1','category2','customer_pn']
    list_filter = ['pn_type','category1','category2']
    list_display = ('rd','pn','pn_type','title','customer_pn','bom','description','category1','category2','critical')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    autocomplete_fields = ['bom']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['rd','pn',('pn_type','critical'),'bom','title','description','category1','category2']}),
        ('Customer Information',{'fields': ['customer_pn']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = BomDetailResource
    inlines             = [AlternatePartInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(Bom_Detail,BomDetailAdmin)




class AlternatePartAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['pn','description','category1','category2','customer_pn']
    list_filter = ['category1','category2','customer_pn']
    list_display = ('ordered','pn','customer_pn','bom_detail','description','category1','category2')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','created_date','modified_date')
    autocomplete_fields = ['bom_detail']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['bom_detail','pn','description','category1','category2']}),
        ('Customer Information',{'fields': ['customer_pn']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date']})
    ]
    # resource_class      = BomDetailResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AlternatePartAdmin, self).save_model(request, obj, form, change)
admin.site.register(Alternate_Part,AlternatePartAdmin)