from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Assembly
from .models import Assembly_Detail
from .models import Assembly_Usage
from bom.models import Bom_Detail
# from .models import Alternate_Part

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class AssemblyResource(resources.ModelResource):
    class Meta:
        model = Assembly
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug' )


class AssemblyDetailInline(admin.TabularInline):
    model = Assembly_Detail
    fields = ['ordered','part','title','critical','status']
    extra = 0
    show_change_link = True
    verbose_name = 'Assembly detail'
    verbose_name_plural = 'Assembly details'
    autocomplete_fields = []
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "part":
            assembly = self.get_object(request,Assembly)
            # print(assembly.product.bom)
            if assembly :
                kwargs["queryset"] = Bom_Detail.objects.filter(bom = assembly.product.bom).order_by('rd')
                # print (kwargs["queryset"])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        # return super(AssemblyDetailInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_object(self, request, model):
        # print(request.META['PATH_INFO'].strip('/').split('/'))
        if request.META['PATH_INFO'].strip('/').split('/')[-1] == 'add':
            return None
        object_id = request.META['PATH_INFO'].strip('/').split('/')[-2]
        # print(object_id)
        # print (object_id)
        return model.objects.get(name=object_id)

class AssemblyAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2','status']
    list_display = ('name','title','product','items_count','category1','category2','status','user')
    readonly_fields = ('user','slug','created_date','modified_date')
    autocomplete_fields = ['product']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2','status']}),
        ('Product Information',{'fields': ['product']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = AssemblyResource
    inlines             = [AssemblyDetailInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AssemblyAdmin, self).save_model(request, obj, form, change)

admin.site.register(Assembly,AssemblyAdmin)



class AssemblyUsageAdmin(admin.ModelAdmin):
    search_fields = ['assembly__name','title','description','category1','category2']
    list_filter = ['category1','category2','status']
    list_display = ('assembly','routingdetail','title','category1','category2','status','user')
    readonly_fields = ('user','created_date','modified_date','slug')
    autocomplete_fields = ['assembly','routingdetail']
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['ordered','assembly','routingdetail','title','description','category1','category2','status']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AssemblyUsageAdmin, self).save_model(request, obj, form, change)

admin.site.register(Assembly_Usage,AssemblyUsageAdmin)




# class BomDetailResource(resources.ModelResource):
#     class Meta:
#         model = Bom_Detail
#         import_id_fields = ('bom','rd','pn',)
#         skip_unchanged = True
#         report_skipped= True
#         exclude = ('user','created_date','modified_date','slug','id' )

# class AlternatePartInline(admin.TabularInline):
#     model = Alternate_Part
#     fields = ['ordered','pn','customer_pn','title']
#     extra = 0
#     verbose_name = 'Alternative Part'
#     verbose_name_plural = 'Alternative Parts'

# class BomDetailAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
#     search_fields = ['rd','pn','bom__name','description','category1','category2','customer_pn']
#     list_filter = ['pn_type','category1','category2']
#     list_display = ('rd','pn','pn_type','customer_pn','bom','description','category1','category2','critical')
#     # list_editable = ('color','move_performa')
#     readonly_fields = ('user','slug','created_date','modified_date')
#     autocomplete_fields = ['bom']
#     save_as = True
#     save_as_continue = True
#     save_on_top =True

#     fieldsets = [
#         ('Basic Information',{'fields': ['rd','pn',('pn_type','critical'),'bom','description','category1','category2']}),
#         ('Customer Information',{'fields': ['customer_pn']}),
#         ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
#     ]
#     resource_class      = BomDetailResource
#     inlines             = [AlternatePartInline]

#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         super(BomDetailAdmin, self).save_model(request, obj, form, change)
# admin.site.register(Bom_Detail,BomDetailAdmin)




# class AlternatePartAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
#     search_fields = ['pn','description','category1','category2','customer_pn']
#     list_filter = ['category1','category2','customer_pn']
#     list_display = ('ordered','pn','customer_pn','bom_detail','description','category1','category2')
#     # list_editable = ('color','move_performa')
#     readonly_fields = ('user','created_date','modified_date')
#     autocomplete_fields = ['bom_detail']
#     save_as = True
#     save_as_continue = True
#     save_on_top =True

#     fieldsets = [
#         ('Basic Information',{'fields': ['bom_detail','pn','description','category1','category2']}),
#         ('Customer Information',{'fields': ['customer_pn']}),
#         ('System Information',{'fields':[('user','created_date'),'modified_date']})
#     ]
#     # resource_class      = BomDetailResource

#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         super(AlternatePartAdmin, self).save_model(request, obj, form, change)
# admin.site.register(Alternate_Part,AlternatePartAdmin)