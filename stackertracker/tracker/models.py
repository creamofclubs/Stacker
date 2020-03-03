from django.db import models

# Create your models here.
class Metals(models.Model):
    metal_short = models.CharField(max_length=3, unique=True)
    metal_name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.metal_name

class Currencies(models.Model):
    currency_short = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.currency_name} - {self.currency_short}'

class Price_List(models.Model):
    metal = models.ForeignKey(Metals, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(decimal_places=3)



class Transactions(models.Model):
    metal_id = models.ForeignKey(Metals, on_delete=models.CASCADE)
    purchase_date = models.DateField()