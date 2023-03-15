import csv
import random

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


from users.models import CustomUser


with open('static/data/users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            user = CustomUser(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            user.save()
            if user.pk:
                print(f'Successfully created user: {row["username"]}')
            else:
                print(f'Failed to create user: {row["username"]}')
        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
