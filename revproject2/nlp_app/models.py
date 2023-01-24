from django.db import models
from torch import nn

# Create your models here.
class SentimentModel(models.Model):
    review = models.TextField()
    


