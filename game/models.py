from django.db import models
from users.models import User
from reviews.models import Review

class GameManager(models.Manager):
    pass


class Game(models.Model):
    title = models.CharField(max_length=255, blank=False)
    subtitle = models.CharField(max_length=255, blank=False)
    main_image = models.ImageField(blank=False)
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    image_4 = models.ImageField(blank=True)
    image_5 = models.ImageField(blank=True)
    image_6 = models.ImageField(blank=True)
    image_7 = models.ImageField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

