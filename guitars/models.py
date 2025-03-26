from django.db import models
from core.models import BaseModel

# Create your models here.
class Guitar(BaseModel):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} - {self.name}"