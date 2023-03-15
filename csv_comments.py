import csv

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from comments.models import Comment
from reviews.models import Review
from users.models import CustomUser


with open('static/data/comments.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            review = Review.objects.get(id=row['review_id'])
            author = CustomUser.objects.get(id=row['author'])
            # Create comment object
            comment = Comment(
                text=row['text'],
                pub_date=row['pub_date'],
                author=author,
                review=review
            )
            comment.save()
            if comment.pk:
                print(f'Successfully created comment: {row["id"]}')
            else:
                print(f'Failed to create comment: {row["id"]}')

        except ObjectDoesNotExist as e:
            print(f'Error: {e}')
        except IntegrityError as e:
            print(f'Error: {e}')
