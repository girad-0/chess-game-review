# from django.db import models

# Create your models here.
from django.db import models


class Review(models.Model):
    white_player = models.CharField(max_length=100)
    black_player = models.CharField(max_length=100)

    event = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=30, blank=True)
    result = models.CharField(max_length=20, blank=True)


    pgn = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.white_player} vs {self.black_player}"