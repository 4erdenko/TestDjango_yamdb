import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from genres.models import Genres

with open('static/data/genre.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # Create genre object
            genre = Genres(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            genre.save()

            print(f'Successfully created title: {row["name"]}')
        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
