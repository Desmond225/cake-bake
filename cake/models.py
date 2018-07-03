from django.db import models
from django.utils import timezone

import datetime


# Create your models here.
class Recipe(models.Model):
    ingredients = models.CharField(max_length=550)
    pub_date = models.DateTimeField('date published')
    # def __str__(self):
    #     return self.recipe_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.rating_text
