from django.shortcuts import render


from django.shortcuts import render
from .models import Titles, Category
from reviews.models import Review
from comments.models import Comment
from genres.models import Genres
def titles_view(request):
    titles = Titles.objects.all()
    categories = Category.objects.all()
    genres = Genres.objects.all()
    context = {
        'titles': titles,
        'categories': categories,
        'genres': genres,
    }
    return render(request, 'index.html', context)
