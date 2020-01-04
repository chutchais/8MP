from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Item
from .models import ItemList
# class ItemListline(admin.):
class ItemListline(admin.TabularInline):
    model = ItemList
    extra = 0
    can_delete = True
    verbose_name_plural = 'Item list configuration'
    fields = ('name','title','value','default','status','modified_date')
    extra = 0 # how many rows to show
    readonly_fields =['modified_date']
    autocomplete_fields = ()
    show_change_link = True



class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['input_type','required','category1','category2']
    list_display = ('name','title','input_type','item_count','required','has_validation_code','category1','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','has_validation_code','created_date','modified_date')
    autocomplete_fields = ['snippet']
    save_as = True
    save_as_continue = True
    save_on_top =True
    


    fieldsets = [
        ('Basic Information',{'fields': ['name','title','required','description',
                            'has_validation_code','category1','category2']}),
        ('Input Type',{'fields': ['input_type','help_text']}),
        ('Text Box Information',{'fields': ['default_value','regexp']}),
        ('Validation Code',{'fields': ['snippet','expected_return']}),
        ('System Information',{'fields':[('user','created_date'),'modified_date','slug']})
    ]
    inlines=[ItemListline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemAdmin, self).save_model(request, obj, form, change)

admin.site.register(Item,ItemAdmin)


class ItemListAdmin(admin.ModelAdmin):
    search_fields = ['name','title','value','item__name']
    list_filter = []
    list_display = ('name','title','value','item','ordered')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','item','slug','user']}),
        ('Value',{'fields': ['value','default']}),
        ('Ordering',{'fields': ['ordered']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemListAdmin, self).save_model(request, obj, form, change)

admin.site.register(ItemList,ItemListAdmin)