import csv
import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from users.models import CustomUser
from reviews.models import Review
from titles.models import Titles

with open('static/data/review.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # Get random author from database
            author = random.choice(CustomUser.objects.all())

            # Get title from database
            title = Titles.objects.get(id=row['title_id'])

            # Create review object
            review = Review(
                id=row['id'],
                text=row['text'],
                score=row['score'],
                pub_date=row['pub_date'],
                author=author,  # assign random author
                title=title
            )
            review.save()
            if review.pk:
                print(f'Successfully created review: {row["id"]}')
            else:
                print(f'Failed to create review: {row["id"]}')

        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
