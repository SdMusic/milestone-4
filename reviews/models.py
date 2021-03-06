from django.db import models

# Create your models here.

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    Review model to allow user to leave a product review
    """
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING)

    def __str__(self):
        return self.title
