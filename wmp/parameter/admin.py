from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from parameter.models import Parameter,ParameterDetail

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class ParameterResource(resources.ModelResource):
    class Meta:
        model = Parameter
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        fields = ('name', 'title', 'description', 
                    'category1', 'category2',  'status')

class ParameterSetInline(admin.TabularInline):
    model = ParameterDetail
    extra = 0 # how many rows to show
    fields =['item','ordered','required','status','modified_date']
    autocomplete_fields =['item']
    readonly_fields = ['modified_date']
    show_change_link = True
    verbose_name = 'Parameter item'
    verbose_name_plural = 'Parameter items'



class ParameterAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description']
    list_filter = []
    list_display = ('name','title','item_count','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    save_as = True
    save_as_continue = True
    save_on_top =True

    inlines=[ParameterSetInline]

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    resource_class      = ParameterResource

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ParameterAdmin, self).save_model(request, obj, form, change)

admin.site.register(Parameter,ParameterAdmin)