from django.db import models
from .models_item import Item
from .models_base import BaseModel

# This is Sale models with BaseModel inheritance.
class SellHeader(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    description = models.TextField(blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class SellDetail(BaseModel):
    header = models.ForeignKey(SellHeader, on_delete=models.CASCADE, related_name='details')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.header.code} - {self.item.code}"