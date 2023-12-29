from django.contrib import admin

from nylasapp.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'created_at', 'updated_at', 'status')
