from django.contrib import admin

from .models import Titles


@admin.register(Titles)
class TitlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year','title_score', 'category',
                    'description',
                    'display_genres']
    list_display_links = ['id', 'name', 'year','title_score', 'category', 'description',
                          'display_genres']
    list_filter = ['genre__name','title_score', 'name', 'year', 'category', ]

    def display_genres(self, obj):
        return ', '.join([genre.name for genre in obj.genre.all()])

    display_genres.short_description = 'Жанр'
