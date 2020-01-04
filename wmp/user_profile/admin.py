from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from user.models import WMPUser,UserAccess
from user_profile.models import Profile,AccessOperation

# from django.contrib.auth.models import Permission
# admin.site.register(Profile)

# from shop.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class OperationInline(admin.TabularInline):
    model = AccessOperation
    can_delete = True
    verbose_name_plural = 'Operation - Authentication'
    extra = 0


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user','title']
    list_filter = ['department','title']
    list_display = ('user','title','department')
    # list_editable = ('color','move_performa')
    # readonly_fields = ('user','slug')
    # formfield_overrides = {
    #     # models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':40})},
    # }

    fieldsets = [
        ('Basic Information',{'fields': ['user','title','department']}),
        
    ]
    inlines = [OperationInline]
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(SnippetAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['code'].widget.attrs['style'] = 'width:800px; height:500px;'
    #     return form

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super(SnippetAdmin, self).save_model(request, obj, form, change)

admin.site.register(Profile,ProfileAdmin)
# from .forms import UserAdminChangeForm
# # UserAdminCreationForm, 
# # # Define a new User admin
# class UserAdmin(BaseUserAdmin):
# 	form = UserAdminChangeForm
# 	list_display = ('username', 'first_name', 'last_name', 'department', 'is_staff')
# 	fieldsets = (
#         ('General', {'fields': ('username', 'first_name', 
#         	'last_name','password',
#         	 'department', )}

#         ),
#         ('Permission',{'fields':('is_active', 'is_staff', 'is_superuser',
#         	'groups', 'user_permissions')}),
      
#     )
# 	inlines = [OperationInline]
# 	# filter_horizontal=['operations']
# 	class Meta:
# 		model = WMPUser
#     # inlines = (EmployeeInline, )

# # Re-register UserAdmin
# # admin.site.unregister(User)
# # admin.site.unregister(User)
# admin.site.register(WMPUser, UserAdmin)