from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class Redcup(models.Model):
    name = models.CharField(max_length=100)
    rules = models.TextField(max_length=2000, default='Put your rules here!')
    players = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'redcup_id': self.id})

class Comment(models.Model):
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.CharField(max_length=1000, default="Enter comment here!")

    redcup = models.ForeignKey(Redcup, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment