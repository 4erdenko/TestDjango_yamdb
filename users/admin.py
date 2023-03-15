from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name']
    list_display_links = ['id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name']
    search_fields = ['id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name']
    list_filter = ['role', 'first_name', 'last_name']
    empty_value_display = '-пусто-'
