"""Admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin model."""
    ordering = ['id']
    list_display = ['name', 'email']
    list_filter = ('is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('permissions',
         {'fields': ('is_active',
                     'is_staff',
                     'is_superuser',)
          }
         ),
        ('Important dates', {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email',
                                                 'password1',
                                                 'password2',
                                                 'is_active',
                                                 'is_staff',
                                                 'is_superuser')}),
    )


admin.site.register(models.User, UserAdmin)
