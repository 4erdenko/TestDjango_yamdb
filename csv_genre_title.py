import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from genres.models import Genres
from titles.models import Titles
with open('static/data/genre_title.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # Create genre object
            title = Titles.objects.get(id=row['title_id'])
            genre = Genres.objects.get(id=row['genre_id'])

            # Add the genre to the title
            title.genre.add(genre)
            title.save()
            if title.pk:
                print(f'Successfully created genre: {row["genre_id"]}')
            else:
                print(f'Failed to create genre: {row["genre_id"]}')

        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
