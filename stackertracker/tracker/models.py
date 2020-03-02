from django.db import models

# Create your models here.
class Metals(models.Model):
    metal = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.metal

class Transactions(models.Model):
    metal_id = models.ForeignKey(Metals, on_delete=models.CASCADE)
    purchase_date = models.DateField()