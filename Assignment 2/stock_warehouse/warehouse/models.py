from django.db import models

# All models from different files are integrated to models.py. Therefore, code will be faster because the program doesn't need to be read until too long lines (like 1000s of lines).
from .models_base import BaseModel
from .models_item import Item
from .models_purchase import PurchaseHeader, PurchaseDetail
from .models_sell import SellDetail, SellHeader