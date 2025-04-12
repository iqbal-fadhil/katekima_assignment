from django.db import models
from .models_item import Item

class PurchaseHeader(models.Model):
    code = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class PurchaseDetail(models.Model):
    header = models.ForeignKey(PurchaseHeader, related_name='details', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit_price = models.FloatField()

    def __str__(self):
        return f"{self.header.code} - {self.item.code}"
