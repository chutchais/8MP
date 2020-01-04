from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Snippet

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


class SnippetResource(resources.ModelResource):
    class Meta:
        model = Snippet
        import_id_fields = ('name',)
        skip_unchanged = True
        report_skipped= True
        exclude = ('id','user','created_date','modified_date','slug',
            'linenos','language','style','highlighted')

class SnippetAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    search_fields = ['name','title','description']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','created_date','modified_date')
    save_as = True
    save_as_continue = True
    save_on_top =True

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description']}),
        ('Category',{'fields': [('category1','category2')]}),
        ('Code',{'fields': ['code']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]

    resource_class      = SnippetResource

    def get_form(self, request, obj=None, **kwargs):
        form = super(SnippetAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['code'].widget.attrs['style'] = 'width:800px; height:500px;'
        return form

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SnippetAdmin, self).save_model(request, obj, form, change)

admin.site.register(Snippet,SnippetAdmin)