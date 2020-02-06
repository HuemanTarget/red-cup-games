from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Redcup(models.Model):
    name = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    # description = models.CharField(max_length=400)
    # price = models.IntegerField()
    # accessorys = models.ManyToManyField(Accessory)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name