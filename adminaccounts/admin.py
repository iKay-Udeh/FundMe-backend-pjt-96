from django.contrib import admin
from .models import AdminAccount
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    list_editable = ('is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(AdminAccount, AccountAdmin)