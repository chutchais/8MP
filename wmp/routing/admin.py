from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Routing,RoutingDetail
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

from assembly.models import Assembly_Usage


class RoutingResource(resources.ModelResource):
    class Meta:
        model = Routing
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug' )

class RoutingDetailInline(admin.TabularInline):
    model = RoutingDetail
    fields = ('position','operation','next_pass','next_fail','title')
    extra = 0 # how many rows to show
    autocomplete_fields = ('operation','next_pass','next_fail')
    show_change_link = True
    verbose_name = 'Routing detail'
    verbose_name_plural = 'Routing detail'

class RoutingAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','operations_count','category1','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = RoutingResource
    inlines = [RoutingDetailInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingAdmin, self).save_model(request, obj, form, change)
admin.site.register(Routing,RoutingAdmin)




from routing.models import (RoutingDetail,RoutingDetailParameterSet,
                                    RoutingDetailAcceptSet,RoutingDetailRejectSet,RoutingDetailNextSet,
                                    RoutingDetailHook)
from routing.models import RoutingDetailAccept
from routing.models import RoutingDetailReject
from routing.models import RoutingDetailOperationChoice



class NextOperationInline(admin.TabularInline):
    model = RoutingDetailNextSet
    extra = 0 # how many rows to show
    fields = ('routingnext','title','ordered','operation','status','modified_date')
    autocomplete_fields =['routingnext']
    readonly_fields = ['modified_date']
    show_change_link = True
    verbose_name = 'Next Operation Condition'
    verbose_name_plural = 'Next Operation Condition'

class HookInline(admin.TabularInline):
    model = RoutingDetailHook
    extra = 0 # how many rows to show
    fields = ('event','name','title','snippet','modified_date')
    readonly_fields = ['modified_date']
    autocomplete_fields =['snippet']
    show_change_link = True
    verbose_name = 'Hook - Local event Configuration'
    verbose_name_plural = 'Hook - Local event Configuration'

class RoutingDetailParameterInline(admin.TabularInline):
    model = RoutingDetailParameterSet
    fields = ('parameter','status','modified_date')
    readonly_fields = ['modified_date']
    autocomplete_fields =['parameter']
    show_change_link = True
    extra = 0 # how many rows to show
    verbose_name = 'Parameter Configuration'
    verbose_name_plural = 'Parameter Configuration'

class AcceptInline(admin.TabularInline):
    model = RoutingDetailAcceptSet
    extra = 0
    fields = ['routingaccept','ordered','status','created_date']
    readonly_fields =['created_date']
    autocomplete_fields =['routingaccept']
    can_delete = True
    show_change_link = True
    verbose_name_plural = 'Routing - Accept'

class RejectInline(admin.TabularInline):
    model = RoutingDetailRejectSet
    extra = 0
    fields = ['routingreject','ordered','status','created_date']
    readonly_fields =['created_date']
    autocomplete_fields =['routingreject']
    can_delete = True
    show_change_link = True
    verbose_name_plural = 'Routing - Reject'

    # Assembly_Usage
class AssemblyInline(admin.TabularInline):
    model = Assembly_Usage
    extra = 0
    fields = ['ordered','assembly','title','status','created_date']
    readonly_fields =['created_date']
    autocomplete_fields =['assembly']
    can_delete = True
    show_change_link = True
    verbose_name_plural = 'Routing - Assembly'

# Operation Choice
class OperationChoiceInline(admin.TabularInline):
    model = RoutingDetailOperationChoice
    extra = 0
    fields = ['ordered','operation','title','status','created_date']
    readonly_fields =['created_date']
    autocomplete_fields =['operation']
    # can_delete = True
    show_change_link = True
    verbose_name_plural = 'Routing - Operation Choice'

class RoutingDetailResource(resources.ModelResource):
    class Meta:
        model = RoutingDetail
        import_id_fields = ('operation','routing',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('user','created_date','modified_date','slug','id' ,'parameter', 'accept_code', 'reject_code', 'next_code')

class RoutingDetailAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['operation','routing__name','description','category1','category2']
    list_filter = ['operation']
    list_display = ('operation','routing','position','next_pass','next_fail','category1','created_date')
    # list_editable = ('color','move_performa')
    autocomplete_fields = ['operation','routing','next_pass','next_fail']
    readonly_fields = ('user','slug','created_date','modified_date')
    save_as = True
    save_as_continue = True
    save_on_top =True
    

    fieldsets = [
        ('Basic Information',{'fields': ['routing',('operation','position'),'description','category1','category2']}),
        ('Next Operation Information (Default)',{'fields': ['next_pass','next_fail']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = RoutingDetailResource
    inlines = [AcceptInline,RejectInline,RoutingDetailParameterInline,
                    NextOperationInline,HookInline,AssemblyInline,
                    OperationChoiceInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetail,RoutingDetailAdmin)


from routing.models import RoutingDetailNext

class RoutingDetailNextAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    autocomplete_fields =['snippet']

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
        ('Next Code',{'fields': ['snippet']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailNextAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetailNext,RoutingDetailNextAdmin)




from routing.models import RoutingDetailAccept


class RoutingDetailAcceptAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    autocomplete_fields =['snippet']
    readonly_fields = ('user','slug','modified_date','user','created_date')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
        ('Accept Code',{'fields': ['snippet']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailAcceptAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetailAccept,RoutingDetailAcceptAdmin)



class RoutingDetailRejectAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    autocomplete_fields =['snippet']
    readonly_fields = ('user','slug','modified_date','user','created_date')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
        ('Except Code',{'fields': ['snippet']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailRejectAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetailReject,RoutingDetailRejectAdmin)




from routing.models import RoutingDetailHook

    
class RoutingDetailHookAdmin(admin.ModelAdmin):
    search_fields = ['name','description','title','event','category1','category2']
    list_filter = ['category1','category2','name','event','routing_detail']
    list_display = ('name','event','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    autocomplete_fields =['snippet']
    

    fieldsets = [
        ('Local Object',{'fields': ['name','title','routing_detail']}),
        ('Event Information',{'fields': ['ordered',('event','snippet')]}),
         ('Basic Information',{'fields': ['description','slug','category1','category2','user']}),
    ]
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailHookAdmin, self).save_model(request, obj, form, change)

admin.site.register(RoutingDetailHook,RoutingDetailHookAdmin)