from django.db import models

class watchList(models.Model):
    watched = models.BooleanField(default = False)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()