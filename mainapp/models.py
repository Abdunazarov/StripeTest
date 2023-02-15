from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()


    def __str__(self) -> str:
        return self.name
    
    

class Order(models.Model):
    items = models.ManyToManyField(Item)



    def overall_price(self):
        price = 0
        for item in self.items.all():
            price += item.price

        return price
    
    
    def __str__(self) -> str:
        return 'Overall price: ' + str(self.overall_price()) + '$'