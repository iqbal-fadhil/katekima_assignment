from django.db import models

# This BaseModel contains the fields that are repeatedly appear on other models. Therefore, those fields don't need to be typed repeatedly.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True