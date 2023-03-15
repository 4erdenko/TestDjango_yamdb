from django.urls import path
from .views import titles_view

app_name = 'titles'

urlpatterns = [
    path('', titles_view, name='titles_list'),
]
