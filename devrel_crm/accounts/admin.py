from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.forms import AdminUserChangeForm, SignUpForm
from accounts.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone_number',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    readonly_fields = (
        'id',
        'date_joined',
        'last_login',
    )
    ordering = ('id', )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'is_email_confirmed',
    )
    form = AdminUserChangeForm
    fieldsets = (
        (
            None,
            {
                'fields': ('email',),
            },
        ),
        (
            'Личная информация', {
                'fields': (
                    'last_name',
                    'first_name',
                    'phone_number',
                ),
            },
        ),
        (
            'Разрешения', {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_email_confirmed',
                ),
            },
        ),
        (
            'Важные даты',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )
    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'password1',
                    'password2',
                ),
            },
        ),
    )
