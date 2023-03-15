import csv
import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from categories.models import Category
from titles.models import Titles
from users.models import CustomUser


with open('static/data/titles.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # Get or create category
            category, _ = Category.objects.get_or_create(
                id=row['category'],
                defaults={
                    'name': f'Category {row["category"]}'})

            # Create title object
            title = Titles(
                name=row['name'],
                description='',
                genre='',
                category=category,
                title_score=0,
                year=row['year']
            )

            # Save title object
            title.save()
            print(f'Successfully created title: {row["name"]}')
        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
