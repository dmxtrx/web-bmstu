from django.db import models

class Product(models.Model):
    cats = [('food', 'еда'),('drink', 'вода'),('snack', 'другое'),]

    name = models.CharField(max_length=200,unique=True,verbose_name='название')
    weight = models.IntegerField(verbose_name='вес в гр')
    price = models.IntegerField(verbose_name='цена в руб')
    category = models.CharField(max_length=20,choices=cats,verbose_name='категория')
    has_allergens = models.BooleanField(default=False,verbose_name='Наличие аллергенов')

    def __str__(self):
        return self.name