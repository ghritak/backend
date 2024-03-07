from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    price = models.IntegerField()
    rating = models.FloatField()
    mrp = models.IntegerField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
