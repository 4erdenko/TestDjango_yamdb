from django.contrib import admin

from genres.models import Genres

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    search_fields = ['id', 'name', 'slug']
    list_filter = ['id', 'name', 'slug']
    empty_value_display = '-пусто-'