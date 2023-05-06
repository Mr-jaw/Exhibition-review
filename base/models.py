from django.db import models


class Reviews(models.Model):
    school = models.CharField(max_length=255)
    review = models.TextField(max_length=1000)
# Create your models here.
