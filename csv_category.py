import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from categories.models import Category

with open('static/data/category.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # Create category object
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )

            # Save category object
            category.save()
            print(f'Successfully created title: {row["name"]}')
        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
