from django.db import models

class Item(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    stock = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.name}"
