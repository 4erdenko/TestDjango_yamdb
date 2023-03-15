from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'score', 'pub_date', 'title']
    list_display_links = ['id', 'text', 'author', 'score', 'pub_date', 'title']
    search_fields = ['id', 'text', 'author', 'score', 'pub_date', 'title']
    list_filter = ['author', 'title']
    empty_value_display = '-пусто-'
