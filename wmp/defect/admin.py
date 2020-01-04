from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import DefectCode,Defect


class DefectCodeAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug',
                                'category1','category2','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(DefectCodeAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(DefectCode,DefectCodeAdmin)

class DefectAdmin(admin.ModelAdmin):
    # search_fields = []
    list_filter = ['defectcode']
    list_display = ('symptom','defectcode','ndf','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ['user']
    fieldsets = [
        ('Basic Information',{'fields': ['symptom','defectcode','ndf','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(DefectAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(Defect,DefectAdmin)