from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Redcup(models.Model):
    name = models.CharField(max_length=100)
    rules = models.TextField(max_length=2000, default='Put your rules here!')
    players = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'redcup_id': self.id})